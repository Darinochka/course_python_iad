import math
from distance import distance
from is_input_in_circle import is_point_in_circle


def is_point_inside_circle(x1, y1):
    x0 = -1
    y0 = 1
    r = 2
    return bool(distance(x1, y1, x0, y0) < r)


def is_point_in_area(x, y):
    d = (x + y >= 0) and (2 * x - y + 2 <= 0)
    k = (x + y <= 0) and (2 * x - y + 2 >= 0)
    in_circ_area = is_point_in_circle(x, y) and d
    in_bottom = not is_point_inside_circle(x, y) and k

    return in_circ_area or in_bottom
