Tutorial
=====

Installation
------------

To use GeoPro, first install it using easy_install or pip:

.. code-block:: console

   $ pip install geopro

.. code-block:: console

   $ easy_install geopro

Run "python setup.py install" in the root directory to install it from source.

GPX to Map data
----------------

To convert the data from a GPX file to a data structure that can be used by online map services,
the developer can use ``load_gpx()`` and ``dump_map_data()`` functions from Mapper class.

For example, the developer can convert the track GPX file recorded by the GPS and make a valid
data file the following way:

>>> import * from geopro
>>> mapper = Mapper()
>>> gpx_file = open('data/gps_info.gpx', 'r')
>>> track = mapper.load_gpx(gpx_file)
>>> file_output = open('data/map_info', 'w+')
>>> mapper.dump_map_data(track, file_output)
