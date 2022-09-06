import math


k = [float(input()) for i in range(3)]

a, b, c = k

d = b ** 2 - (4 * a * c)

if d < 0:
    print(0)

elif d == 0:
    x = -b / (2 * a)
    print(1, x)

else:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print(2, min(x1, x2), max(x1, x2))
