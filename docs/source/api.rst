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
   :param elevation: Optional elevation value.
   :type elevation: float or None


   .. py:method:: get_point_coordinates():

      Return a list of random ingredients as strings.

      :param kind: Optional "kind" of ingredients.
      :type kind: list[str] or None
      :return: The ingredients list.
      :rtype: list[str]