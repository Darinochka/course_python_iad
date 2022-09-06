from distance import distance


def is_point_in_circle(x1, y1, x0, y0, r):
    return distance(x1, y1, x0, y0) <= r
