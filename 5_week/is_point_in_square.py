def is_point_in_square(x, y):
    is_in = abs(x) <= 1 and abs(y) <= 1
    return is_in * "YES" + (1 - is_in) * "NO"


x1, y1 = float(input()), float(input())
print(is_point_in_square(x1, y1))