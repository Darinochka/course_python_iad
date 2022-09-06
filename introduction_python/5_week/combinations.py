def combinations(n, k):
    if k == 0 or n == k:
        return 1
    if k == 1:
        return n
    return combinations(n-1, k-1) + combinations(n-1, k)