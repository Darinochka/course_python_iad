def is_point_in_square(x, y):
    is_in = abs(x) <= 1-y and abs(x) <= 1+y and\
            abs(y) <= 1-x and abs(y) <= 1+x

    return is_in * "YES" + (1 - is_in) * "NO"


coord = [float(input()) for i in range(2)]

print(is_point_in_square(*coord))