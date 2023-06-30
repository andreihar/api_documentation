Reference
===

.. autosummary::
   :toctree: generated

   lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']



Channel
=======

Channel
-------
.. class:: Noodle
   :members: eat, slurp
   :inherited-members:
   :member-order: bysource

   .. method:: boil(time=10)
      Boil the noodle *time* minutes.