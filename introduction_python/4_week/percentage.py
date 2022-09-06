data = [int(input()) for i in range(3)]

p, x, y = data

d = (x * 100 + y) * p * 0.01 + x * 100 + y

print(int(d // 100), int(d % 100))
