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


Farthest apart points
----------------

GeoPro provides good basic methods to operate on geographic points, which the developers can use
to perform advanced operations. For example, by using the ``compare_distance()`` method of the
Point class, the developer can find two points that are farthest apart in the list:

>>> from geopro import *
>>> points = [
      Point(51.73111, -0.62872),
      Point(51.74472, 0.38751),
      Point(51.20069, -0.74408),
      Point(51.20413, 0.49738)
      ]
>>> max_dist = 0
>>> for i in range(0, len(points)):
>>>     for j in range(0, len(points)):
>>>         if points[i].compare_distance(points[j]) > max_dist:
>>>             point1 = points[i]
>>>             point2 = points[j]
>>> print(max_dist)
1.255573
>>> print(point1.get_point_coordinates())
[51.74472, 0.38751]
>>> print(point2.get_point_coordinates())
[51.20069, -0.74408]


Sort information based on location
----------------

By using GeoPro, developers can check weather any computer information that includes geographic point data
is related to any particular place by using the ``is_point_inside()`` method of the Polygon class.
For this, the developer has to define the polygon of a desired place. In this example, we import a GPX file which defines Canada.

>>> import * from geopro
>>> mapper = Mapper()
>>> gpx_file = open('data/canada.gpx', 'r')
>>> canada_polygon = mapper.load_gpx(gpx_file)

Then, we extract the geographic point information either manually, or by using the help of other scraping libraries.
Now, we define a geographic point with GeoPro class Point

>>> point = Point(49.22659, -123.02378)

Finally, check if the point of interest is within the polygon.

>>> canada_polygon.is_point_inside(point)
True

If it isn't the returned value will be False.

>>> point = Point(51.73111, -0.62872)
>>> canada_polygon.is_point_inside(point)
False


GPX to Data structure
----------------

When loading GPX file, GeoPro automatically detects the type of the information stored in the
GPX file and returns created instance of the appropriate object. Since it may not always be correct,
the developer can extract points from the data structure and create a new one using extracted points.

>>> import * from geopro
>>> mapper = Mapper()
>>> gpx_file = open('data/gps_info.gpx', 'r')
>>> incorrect_structure = mapper.load_gpx(gpx_file)
>>> points = incorrect_structure.get_points() # created Track object
>>> print(points)
[
   Point(51.73111, -0.62872),
   Point(51.74472, 0.38751),
   Point(51.20069, -0.74408),
   Point(51.20413, 0.49738)
]
>>> track = Polygon(points) # fixed to Polygon object


GPX to Map data
----------------

To convert the data from a GPX file to a data structure that can be used by online map services,
the developer can use ``load_gpx()`` and ``dump_map_data()`` methods from Mapper class.

For example, the developer can convert the track GPX file recorded by the GPS and make a valid
data file the following way:

>>> import * from geopro
>>> mapper = Mapper()
>>> gpx_file = open('data/gps_info.gpx', 'r')
>>> track = mapper.load_gpx(gpx_file)
>>> file_output = open('data/map_info', 'w+')
>>> mapper.dump_map_data(track, file_output)
