n = int(input())
x = float(input())
res = 0

while n > 0:
    coef = float(input())
    res += coef
    res *= x
    n -= 1

coef = float(input())
res += coef
print(res)