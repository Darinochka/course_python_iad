def min_divisor(n):
    min_d = 2

    if n % min_d == 0:
        return 2
    
    min_d = 3
    while min_d ** 2 <= n:
        if n % min_d == 0:
            return min_d
        min_d += 2
    return n


def is_prime(n):
    return min_divisor(n) == n


n = int(input())
print("YES" * is_prime(n) + "NO" * (1 - is_prime(n)))