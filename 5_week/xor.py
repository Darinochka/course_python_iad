def xor(x, y):
    return int(bool(x) != bool(y))


data = [int(input()) for i in range(2)]

print(xor(*data))