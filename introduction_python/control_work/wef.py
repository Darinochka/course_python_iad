n = int(input())
m = int(input())

# rest = m % n
# if rest != 0:
#     k = (m - rest) // (n - 1)
#     print(k) if k > rest else print(rest)
# else:
#     print(m // n)

print(m // n) if m % n == 0 else print(m // n + 1)