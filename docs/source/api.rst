API
===

I write something new

.. py:class:: Point(latitude, longitude, elevation=None):

   Instantiates a geographic point object. By defining latitude and longitude makes it a 2D point.
   Defining the optional elevation parameter makes it a 3D point.

   :param latitude: latitude value between -90 to 90.
   :type latitude: float
   :param longitude: longitude value between -180 to 180.
   :type longitude: float
   :param elevation: Optional elevation value in metres.
   :type elevation: int or None


   .. py:method:: get_point_coordinates(point):

      Return a list of coordinates of the geographic point.

      :param point: Optional "kind" of ingredients.
      :type kind: Point
      :return: Coordinates of the geographic point.
      :rtype: list

      >>> point2d = Point(51.5072, -0.1276)
      >>> get_point_coordinates(point2d)
      [51.5072, -0.1276]
      >>> point3d = Point(51.5072, -0.1276, 25)
      >>> get_point_coordinates(point3d)
      [51.5072, -0.1276, 25]