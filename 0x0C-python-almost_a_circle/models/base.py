#!/usr/bin/python3
"""ClassThis class will be the “base” of all other classes in this project."""


class Base:
    """Represent the base model"""
    __nb_object = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
