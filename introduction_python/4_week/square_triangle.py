import math


sides = [float(input()) for i in range(3)]

p = sum(sides) / 2
a, b, c = sides

s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(round(s, 6))
