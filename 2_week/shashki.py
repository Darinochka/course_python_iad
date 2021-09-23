x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

white_is_1 = (x1 + y1) % 2 == 0            # cheking original black square
white_is_2 = (x2 + y2) % 2 == 0            # move to only black square

if (white_is_1 and white_is_2 and y2 > y1 and
        (y2 - y1 >= abs(x2 - x1))):
    # moving
    print("YES")
else:
    print("NO")
