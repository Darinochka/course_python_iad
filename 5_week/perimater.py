import itertools
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def perimetr(coord):
    sides = []
    for i in itertools.combinations(coord, 2):
        sides.append(distance(*i[0], *i[1]))
    return sum(sides)


coord = [[int(input()) for i in range(2)] for j in range(3)]

print(perimetr(coord))