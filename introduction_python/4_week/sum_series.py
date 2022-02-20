n = int(input())

s = 0
for i in range(1, n+1):
    s += 1 / i ** 2

print(round(s, 6)) if n != 1 else print(1)