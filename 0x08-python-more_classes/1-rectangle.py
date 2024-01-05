#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(value) is int:
            self._width = value
        else:
            raise TypeError("width must be an integer")
        if value > 0:
            self._width = value
        else:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if type(value) is int:
            self._height = value
        else:
            raise TypeError("height must be an integer")
        if value > 0:
            self._height = value
        else:
            raise ValueError("height must be >= 0")
