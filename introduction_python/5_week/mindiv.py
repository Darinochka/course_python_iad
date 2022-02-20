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