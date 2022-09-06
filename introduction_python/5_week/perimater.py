import itertools
from distance import distance


def perimetr(coord):
    sides = []
    for i in itertools.combinations(coord, 2):
        sides.append(distance(*i[0], *i[1]))
    return sum(sides)