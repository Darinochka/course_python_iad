a, b, c = int(input()), int(input()), int(input())

sides = sorted([a, b, c])

if sides[2] >= sides[1] + sides[0]:
    print("impossible")
elif sides[2] ** 2 > sides[1] ** 2 + sides[0] ** 2:
    print("obtuse")
elif sides[2] ** 2 < sides[1] ** 2 + sides[0] ** 2:
    print("acute ")
else:
    print("rectangular")
