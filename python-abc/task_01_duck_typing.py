#!/usr/bin/python3
"""
Defines shapes using abstract base classes and demonstrates duck typing.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius):
        """Initialize circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return 3.141592653589793 * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """Rectangle shape defined by width and height."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
