def gen_squared(x):
    for i in range(1, x + 1):
        if i * i < x + 1:
            yield i * i
        else:
            break


n = int(input())

for i in gen_squared(n):
    print(i, end=" ")
