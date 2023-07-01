Reference
=====

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
      :type return: list

      >>> point2d = Point(51.5072, -0.1276)
      >>> point2d.get_point_coordinates()
      [51.5072, -0.1276]
      >>> 
      >>> point3d = Point(51.5072, -0.1276, 25)
      >>> point3d.get_point_coordinates()
      [51.5072, -0.1276, 25]


   .. py:method:: convert_point_dimension(elevation):

      Converts a 3D point to a 2D if elevation is set to None.

      Converts a 2D point to a 3D if elevation is set to integer.

      :param elevation: elevation value of the point coordinates.
      :type elevation: int or None
      :return: modified geographic point
      :type return: Point

      >>> point2d = Point(51.5072, -0.1276)
      >>> point2d.get_point_coordinates()
      [51.5072, -0.1276]
      >>> 
      >>> point3d = point2d.convert_point_dimension(25)
      >>> point3d.get_point_coordinates()
      [51.5072, -0.1276, 25]
      >>>
      >>> point2d2 = point3d.convert_point_dimension(None)
      >>> point2d2.get_point_coordinates()
      [51.5072, -0.1276]

   
   .. py:method:: compare_distance(point):

      Compares and returns the difference between two geographic points.

      When comparing 2D with a 3D point, the 3D point will be converted to a 2d point.

      :param point: elevation value of the point coordinates.
      :type point: Point
      :return: distance between two points
      :type return: float

      >>> point1 = Point(51.5072, -0.1276)
      >>> point2 = Point(51.7311, -0.6287)
      >>> point1.compare_distance(point2)
      0.548846
      >>> 
      >>> point1 = Point(51.5072, -0.1276, 17)
      >>> point2 = Point(51.7311, -0.6287, 10)
      >>> point1.compare_distance(point2)
      7.021484
      >>>
      >>> point1 = Point(51.5072, -0.1276)
      >>> point2 = Point(51.7311, -0.6287, 10)
      >>> point1.compare_distance(point2)
      0.548846


Polygon
------------

The Polygon class adds functionality for a geographic region, that can be specified by using a collection of Point instances.
Works for both 2D and 3D geographic points.

.. py:class:: Polygon(points):

   Instantiates a geographic region object. Requires the list of point to have at least 3 points.

   Throws BadPolygonException if it is impossible to define a polygon with given points.

   :param points: points that define a geographic region.
   :type points: list[Point]


   .. py:method:: is_point_inside(point):

      Checks if the given point located within the polygon.
      If polygon is defined with 2D points, the input point will be converted to a 2D geographic point.

      :param point: Optional "kind" of ingredients.
      :type point: Point
      :return: True if point within defined polygon. False otherwise.
      :type return: bool

      >>> points2d = [
         Point(51.73111, -0.62872),
         Point(51.74472, 0.38751),
         Point(51.20069, -0.74408),
         Point(51.20413, 0.49738)
      ]
      >>> polygon2d = Polygon(points2d)
      >>> point3d = Point(51.5072, -0.1276, 25)
      >>> polygon2d.is_point_inside(point3d)
      True
      >>> 
      >>> points3d = [
         Point(51.73111, -0.62872, 1),
         Point(51.74472, 0.38751, 1),
         Point(51.20069, -0.74408, 0),
         Point(51.20413, 0.49738, 0)
      ]
      >>> polygon3d = Polygon(points3d)
      >>> polygon3d.is_point_inside(point3d)
      False


Track
------------

The Track class adds functionality for a geographic track, that can be specified by using a collection of Point instances.
Works for both 2D and 3D geographic points.

.. py:class:: Track(points):

   Instantiates a geographic track object. Requires the list of point to have at least 2 points.

   Throws BadTrackException if it is impossible to define a polygon with given points.

   :param points: points that define a geographic track.
   :type points: list[Point]


   .. py:method:: is_point_on_track(point, error_diameter=0):

      Checks if the given point located within the track path.
      If polygon is defined with 2D points, the input point will be converted to a 2D geographic point.

      By default checks if the point is exactly on the track path. Can be made less strict by specifying the diameter around the track where the point can be located.

      :param point: Optional diameter around the track path where the point can be located. .
      :type point: Point
      :param error_diameter: Optional diameter value around the track path where the point can be located. Specified in degrees just like latitude and longitude.
      :type error_diameter: float
      :return: True if point within defined path. False otherwise.
      :type return: bool

      >>> points = [
         Point(51.73111, -0.62872),
         Point(51.73111, 0.38751)
      ]
      >>> track = Track(points)
      >>> point = Point(51.73000, 0.00000)
      >>> track.is_point_on_track(point)
      False
      >>>
      >>> track_with_error = Track(points, 0.01)
      >>> track_with_error.is_point_on_track(point)
      True


   .. py:method:: complete_path():

      asd

      :return: filled in gaps of the track
      :type return: list[Point]

      >>> points = [
         Point(51.73111, -0.62872),
         Point(51.73111, 0.38751)
      ]
      >>> track = Track(points)
      >>> point = Point(51.73000, 0.00000)
      >>> track.is_point_on_track(point)
      False
      >>>
      >>> track_with_error = Track(points, 0.01)
      >>> track_with_error.is_point_on_track(point)
      True


Mapper
------------

The Mapper class adds functionality for a geographic track, that can be specified by using a collection of Point instances.
Works for both 2D and 3D geographic points.

.. py:class:: Mapper():

   Instantiates a geographic track object. Requires the list of point to have at least 2 points.

   Throws BadTrackException if it is impossible to define a polygon with given points.


   .. py:method:: dump_map_data(input, output_file):

      Converts an input to an output file that can be used for map applications.

      :param input: Optional diameter around the track path where the point can be located. .
      :type input: Point, Polygon, Track
      :param output_file: Optional diameter value around the track path where the point can be located. Specified in degrees just like latitude and longitude.
      :type output_file: string, TextIOWrapper

      >>> points = [
         Point(51.73111, -0.62872),
         Point(51.73111, 0.38751)
      ]
      >>> track = Track(points)
      >>> mapper = Mapper()
      >>> mapper.dump_map_data(track, 'data/map_info1')
      >>> file_output = open('data/map_info2', 'w+')
      >>> mapper.dump_map_data(track, file_output)


   .. py:method:: load_gpx(gpx_file):

      Reads the specified GPX file and stores it in the given data structure. 

      :param gpx_file: Optional diameter around the track path where the point can be located.
      :type gpx_file: string, TextIOWrapper
      :return: returns the data stored in the data structure that GeoPro automatically detected.
      :type return: Point, Polygon, Track

      >>> mapper = Mapper()
      >>> mapper.load_gpx('data/map_info.gpx')
      [
         Point(51.73111, -0.62872),
         Point(51.73111, 0.38751)
      ]
      >>> gpx_file = open('data/map_info2', 'r')
      >>> mapper.load_gpx(gpx_file)
      Point(51.5072, -0.1276, 25)