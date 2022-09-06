def is_palindrom(orig_n):
    result_n = 0
    n = orig_n
    while n > 0:
        s = n % 10
        n = (n - n % 10) // 10
        result_n = result_n * 10 + s

    return (result_n == orig_n)


n = int(input())

i = 1
q = 0

while i <= n:
    if is_palindrom(i):
        q += 1
    i += 1

print(q)