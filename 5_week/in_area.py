import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def is_point_in_circle(x1, y1):
    x0 = -1
    y0 = 1
    r = 2
    return bool(distance(x1, y1, x0, y0) <= r)


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


x, y = float(input()), float(input())

if is_point_in_area(x, y):
    print("YES")
else:
    print("NO")