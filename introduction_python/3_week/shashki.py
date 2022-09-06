x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if abs(y2 - y1) == 1 and x2 - x1 == 1:
    print("YES")
else:
    print("NO")