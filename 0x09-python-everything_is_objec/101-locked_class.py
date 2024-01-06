#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if hasattr(self, name) and name != 'first_name':
            raise AttributeError(f"Cannot add attribute '{name}'")
        else:
            self.__dict__[name] = value
