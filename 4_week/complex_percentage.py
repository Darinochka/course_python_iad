data = [int(input()) for i in range(4)]

p, x, y, k = data

d = x * 100 + y

for i in range(k):
    d = int(d * p * 0.01 + d)

print(int(d // 100), int(d % 100))
