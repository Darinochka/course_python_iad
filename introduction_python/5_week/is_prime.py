from mindiv import min_divisor


def is_prime(n):
    return min_divisor(n) == n
