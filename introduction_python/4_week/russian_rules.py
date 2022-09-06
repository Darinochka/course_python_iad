from math import floor, ceil


x = float(input())

if round(x - floor(x), 6) == 0.5:
    print(ceil(x))
else:
    print(round(x))