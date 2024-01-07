#!/usr/bin/python3
"""
Defining an empty class Rectangle
"""


class Rectangle:

    """Representation of Rectangle"""
    def _init_(self, width=0, height=0):
        """Initialize the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property width to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private property width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private property height"""
        return self.__height

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
