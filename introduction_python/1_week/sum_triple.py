n = int(input())

q = 0
while n != 0:
    q += n % 10
    n = (n - n % 10) // 10

print(q)
