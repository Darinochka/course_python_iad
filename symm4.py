n = int(input())

new = n % 10 * 1000 + n // 10 % 10 * 100 + n // 100 % 10 * 10 + n // 1000

print(n - new + 1)