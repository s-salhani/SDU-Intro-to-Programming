def rectangle_parametter(width : float, lenght : float) -> float:
    """Computes the perimeter of a rectangle given the length and width
    Preconditions:
        width > 0
        length > 0

    >>> rectangle_parameter(5.0, 4.0)
    18.0
    """"

    return 2 * (width + length)




# or

from math import sin as sn, radians as rd

def square_func(x : float) -> float:
    """ returns the area of a square"""
    return(x**2)

def rectangle_func(x : float, y : float) -> float:
    """ returns the area of an rectangle"""
    return(x*y)

def rhombuses_func(x : float, y : float, type : str) -> float:
    """ returns the area of a rhombus.

    mode == "diagnoal": x and y are the two diagonal
    mode == "side_height":
    mode == "side_angle":


    precondition: x > 0, y > 0"""
    
    if type == "diagnol"
        return rectangle_func(x, y)*0.5
    if type == "side_hegiht"
        return rectangle_func(x, y)
    if type == "side_angle"
        return rectangle_func(x, y)



