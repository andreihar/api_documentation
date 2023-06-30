"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

class Point:
    def __init__(self, latitude, longitude, elevation=0.0):
        """Instantiates a geographic point object. By defining latitude and longitude makes it a 2D point. Defining the optional elevation parameter makes it a 3D point.

        Args:
            latitude (float): latitude value between -90 to 90.
            longitude (float): longitude value between -180 to 180.
            elevation (float, optional): elevation value in metres. Defining the variable turns a 2D point to a 3D point.
        """
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def get_point_coordinates(self):
        """Returns the coordinates of the geographic point as a tuple. If a point is 2D, returns latitude and longitude. If a point is 3D, also returns elevation.

        Returns:
            tuple: all coordinate values of the geographic point.
        """
        return [self.latitude, self.longitude, self.elevation]
    
    class InvalidValueError(Exception):
        """Raised if the value for latitude or longitude is out of boundaries."""
        pass