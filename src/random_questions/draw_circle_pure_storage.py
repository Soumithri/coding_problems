"""Implement a method to draw a circle. You are not allowed to use math
library functions such as sqrt, sin, or cos.

For example, given r = 2 (radius), return the following points to plot:

(0,0), (0,1),(0,2), (1,0), (1,1), (2,0), (0,-1),
(0,-2), (-1,0), (-1,1), (1,-1), (-1,-1),(-2,0)
Note that all points satisfy the equation: x^2 + y^2 <= r^2.
"""


def return_circle_points(radius):
    if not radius:
        raise Exception('Radius is a requirement argument for this function')
    result = []
    for i in range(-radius, radius+1):
        for j in range(radius, -radius-1, -1):
            if ((i**2) + (j**2)) <= radius**2: 
                result.append((i, j))
    return result
