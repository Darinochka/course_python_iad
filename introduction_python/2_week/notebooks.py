import itertools
from functools import reduce


def max_q_notebooks(size_room, size_notebook):
    max_q = 0
    for x in itertools.permutations(size_notebook):
        q = reduce(lambda z, d: z * d, [x // y for x, y in zip(size_room, x)])
        if q > max_q:
            max_q = q
    return max_q


size_room = [int(input()) for i in range(3)]
size_notebook = [int(input()) for i in range(3)]

print(max_q_notebooks(size_room, size_notebook))