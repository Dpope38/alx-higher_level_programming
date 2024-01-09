#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """A class that derive from the built-in list object"""

    def print_sorted(self):
        """Define a method that print the list, but sorted"""
        print(sorted(self))
