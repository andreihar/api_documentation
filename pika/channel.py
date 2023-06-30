"""The Channel class provides a wrapper for interacting with RabbitMQ
implementing the methods and behaviors for an AMQP Channel.

"""
# disable too-many-lines
# pylint: disable=C0302

import collections
import logging
import uuid
from enum import Enum

import pika.frame as frame
import pika.exceptions as exceptions
import pika.spec as spec
import pika.validators as validators
from pika.compat import unicode_type, dictkeys, is_integer
from pika.exchange_type import ExchangeType

LOGGER = logging.getLogger(__name__)

MAX_CHANNELS = 65535  # per AMQP 0.9.1 spec.


class Channel(object):
    """A Channel is the primary communication method for interacting with
    RabbitMQ. It is recommended that you do not directly invoke the creation of
    a channel object in your application code but rather construct a channel by
    calling the active connection's channel() method.

    """

    # Disable pylint messages concerning "method could be a function"
    # pylint: disable=R0201

    CLOSED = 0
    OPENING = 1
    OPEN = 2
    CLOSING = 3  # client-initiated close in progress

    _STATE_NAMES = {
        CLOSED: 'CLOSED',
        OPENING: 'OPENING',
        OPEN: 'OPEN',
        CLOSING: 'CLOSING'
    }

    _ON_CHANNEL_CLEANUP_CB_KEY = '_on_channel_cleanup'

    def __init__(self, connection, channel_number, on_open_callback):
        """Create a new instance of the Channel

        :param pika.connection.Connection connection: The connection
        :param int channel_number: The channel number for this instance
        :param callable on_open_callback: The callback to call on channel open.
            The callback will be invoked with the `Channel` instance as its only
            argument.

        """
        if not isinstance(channel_number, int):
            raise exceptions.InvalidChannelNumber(channel_number)

        validators.rpc_completion_callback(on_open_callback)

        self.channel_number = channel_number
        self.callbacks = connection.callbacks
        self.connection = connection

        # Initially, flow is assumed to be active
        self.flow_active = True

        self._content_assembler = ContentFrameAssembler()

        self._blocked = collections.deque(list())
        self._blocking = None
        self._has_on_flow_callback = False
        self._cancelled = set()
        self._consumers = dict()
        self._consumers_with_noack = set()
        self._on_flowok_callback = None
        self._on_getok_callback = None
        self._on_openok_callback = on_open_callback
        self._state = self.CLOSED

        # We save the closing reason exception to be passed to on-channel-close
        # callback at closing of the channel. Exception representing the closing
        # reason; ChannelClosedByClient or ChannelClosedByBroker on controlled
        # close; otherwise another exception describing the reason for failure
        # (most likely connection failure).
        self._closing_reason = None  # type: None | Exception

        # opaque cookie value set by wrapper layer (e.g., BlockingConnection)
        # via _set_cookie
        self._cookie = None

    def __int__(self):
        """Return the channel object as its channel number

        :rtype: int

        """
        return self.channel_number

    def __repr__(self):
        return '<%s number=%s %s conn=%r>' % (
            self.__class__.__name__, self.channel_number,
            self._STATE_NAMES[self._state], self.connection)

    def add_callback(self, callback, replies, one_shot=True):
        """Pass in a callback handler and a list replies from the
        RabbitMQ broker which you'd like the callback notified of. Callbacks
        should allow for the frame parameter to be passed in.

        :param callable callback: The callback to call
        :param list replies: The replies to get a callback for
        :param bool one_shot: Only handle the first type callback

        """
        for reply in replies:
            self.callbacks.add(self.channel_number, reply, callback, one_shot)