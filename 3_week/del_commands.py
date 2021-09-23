a, b = int(input()), int(input())

while a != b:
    if a % 2 != 0 or a // b == 1:
        a -= 1
        print("-1")
    else:
        a /= 2
        print(":2")