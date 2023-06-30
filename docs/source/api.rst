API
===

Point
------------

The Point class defines 2D or 3D geographic points. It allows the developers to keep track of coordinates for the geographic points and makes using other methods of GeoPro simpler.

.. py:class:: Point(latitude, longitude, elevation=None):

   Instantiates a geographic point object. Defining latitude and longitude makes it a 2D point.
   Defining the optional elevation parameter makes it a 3D point.

   Throws IncorrectValueException if either latitude or longitude value isn't defined within range.

   :param latitude: latitude value between -90 to 90.
   :type latitude: float
   :param longitude: longitude value between -180 to 180.
   :type longitude: float
   :param elevation: Optional elevation value in metres.
   :type elevation: int or None


   .. py:method:: get_point_coordinates():

      Return a list of coordinates of the geographic point.

      :return: Coordinates of the geographic point.
      :rtype: list

      >>> point2d = Point(51.5072, -0.1276)
      >>> point2d.get_point_coordinates()
      [51.5072, -0.1276]
      >>> point3d = Point(51.5072, -0.1276, 25)
      >>> point3d.get_point_coordinates()
      [51.5072, -0.1276, 25]


Polygon
------------

The Polygon class adds functionality for a geographic region, that can be specified by using a collection of Point instances.
Works for both 2D and 3D geographic points.

.. py:class:: Polygon(points):

   Instantiates a geographic region object. Requires the list of point to have at least 3 points.

   Throws BadPolygonException if it is impossible to define a polygon with given points.

   :param points: points that define a geographic region.
   :type latitude: list[Point]


   .. py:method:: is_point_inside(point):

      Checks if the given point located within the polygon.
      If polygon is defined with 2D points, the input point will be converted to a 2D geographic point.

      :param point: Optional "kind" of ingredients.
      :type kind: Point
      :return: True if point within defined polygon. False otherwise.
      :type return: bool

      >>> london_points2d = [
         Point(51.73111, -0.62872),
         Point(51.74472, 0.38751),
         Point(51.20069, -0.74408),
         Point(51.20413, 0.49738)
      ]
      >>> london_polygon2d = Polygon(london_points)
      >>> point3d = Point(51.5072, -0.1276, 25)
      >>> london_polygon2d.is_point_inside(point3d)
      True
      >>> 
      >>> london_points3d = [
         Point(51.73111, -0.62872, 1),
         Point(51.74472, 0.38751, 1),
         Point(51.20069, -0.74408, 0),
         Point(51.20413, 0.49738, 0)
      ]
      >>> london_polygon3d.is_point_inside(point3d)
      False


Mapper
------------

The Mapper class 