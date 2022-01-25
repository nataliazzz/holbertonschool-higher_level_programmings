#!/usr/bin/python3
"""
module with a rectangle that does nothing
"""


class Rectangle:
    """
    empty rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        checks the parameters and initializes some values
        Args:
            width (:obj:`int`, optional): width of the Rectangle.
            height (:obj:`int`, optional): height of the Rectangle.
        """

        self.__check_valid_width(width)
        self.__check_valid_height(height)

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        parameters and size of the rectangle
        Args:
            value (int): width of the rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """

        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):
        """
        width of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        parameters and size of the Rectangle
        Args:
            value (int): height of the rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """

        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):
        """
        checks if width is a valid integer
        Args:
            width (int): width of the rectangle.
        Raises:
            TypeError: If `width` type is not `int`.
            ValueError: If `width` is less than `0`.
        """

        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):
        """
        checks if height is a valid integer
        Args:
            height (int): The height of the Rectangle.
        Raises:
            TypeError: If `height` type is not `int`.
            ValueError: If `height` is less than `0`.
        """

        if self.__check_int_value(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive_value(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value):
        """
        checks if value is an integer
        Args:
            value (int): number to verify
        Returns:
            int: If is a int `True`, `False` otherwise.
        """

        if type(value) is int:
            return True

        return False

    def __check_positive_value(self, value):
        """
        checks if value is a positive integer
        Args:
            value (int): number to verify
        Returns:
            int: `True` If value is greater than
            or equal to 0, `False` otherwise.
        """

        if value >= 0:
            return True

        return False
