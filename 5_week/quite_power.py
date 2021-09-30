# Возводить в степень можно гораздо быстрее, чем за n умножений!
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
# an=(a2)n/2 при четном n, an=a⋅ an-1 при нечетном n.
# Реализуйте алгоритм быстрого возведения в степень. Если вы все
# сделаете правильно, то сложность вашего алгоритма будет O(logn).


def quite_power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return quite_power(a * a, n//2)
    else:
        return a * quite_power(a, n-1)


def power(a, n):
    if n >= 0:
        return quite_power(a, n)
    return 1/(quite_power(a, -n))


a, n = float(input()), int(input())

print(power(a, n))