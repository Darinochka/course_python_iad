x = float(input())
y = float(input())
q = 1


while x < y:
    x += 0.1 * x
    q += 1

print(q)
