import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def is_point_in_circle(x1, y1, x0, y0, r):
    if distance(x1, y1, x0, y0) <= r:
        return "YES"
    return "NO"


coord = [float(input()) for i in range(5)]

print(is_point_in_circle(*coord))
