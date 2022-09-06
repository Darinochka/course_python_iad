def is_point_in_square(x, y):
    is_in = abs(x) <= 1-y and abs(x) <= 1+y and\
            abs(y) <= 1-x and abs(y) <= 1+x

    return is_in
