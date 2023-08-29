import math


def area(radius):
    if type(radius) is not int and type(radius) is not float:
        raise TypeError("Invalid Value")
    if radius < 0:
        raise ValueError('Must not be less than 0')
    return math.pi * (radius ** 2)
