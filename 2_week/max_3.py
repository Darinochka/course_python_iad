a = int(input())
b = int(input())
c = int(input())


def max_3(a, b, c):
    if a > b:
        if a > c:
            return a
    else:
        if b > c:
            return b
    return c


print(max_3(a, b, c))
