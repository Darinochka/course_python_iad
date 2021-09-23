data = [int(input()) for i in range(4)]

a, b, c, d = data

if a == 0 and b == 0:
    print('INF')
elif a == 0 or b * c == a * d:
    print('NO')
elif b % a == 0:
    print(-b // a)
else:
    print('NO')