#!/usr/bin/python3
""" The Function that returns available attributes and methods of an object"""


def lookup(obj):
    """Returns lists of available attributes and methods of an object"""
    return dir(obj)
