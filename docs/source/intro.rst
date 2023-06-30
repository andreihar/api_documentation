Intro
=====

.. _installation:

Installation
------------

To use GeoPro, first install it using easy_install or pip:

.. code-block:: console

   (.venv) $ pip install geopro

.. code-block:: console

   (.venv) $ easy_install geopro

Run "python setup.py install" in the root directory to install it from source.

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