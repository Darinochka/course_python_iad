a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
    print(5)
elif b == 0 and d == 0:
    if a != 0:
        print(3, e / a)
    else:
        print(3, f / c)
elif a == 0 and c == 0:
    if b != 0:
        print(4, e / b)
    else:
        print(4, f / d)
elif a * d == b * c and a * f == c * e:
    if b != 0:
        print(1, -a / b, e / b)
    else:
        print(1, -c / d, f / d)
elif a * d == b * c and a * f != c * e:
    print(0)
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print(2, x, y)