#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
"""


class MyList(list):
    """Class that inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
