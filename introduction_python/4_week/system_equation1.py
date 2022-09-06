import numpy as np

a, b = [float(input()) for i in range(2)]
c, d = [float(input()) for i in range(2)]

e, f = [float(input()) for i in range(2)]

x = (e * d - b * f) / (a * d - b * c)
y = (a * f - e * c) / (a * d - b * c)

print(x, y)