k, m, n = int(input()), int(input()), int(input())

if k > n:
    print(2 * m)
else:
    d = n * 2 // k
    d = d + 1 if n * 2 % k > 0 else d
    print(m * d)