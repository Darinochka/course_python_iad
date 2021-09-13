def gen_squared(x):
    for i in range(1, x):
        if i * i <= x:
            yield i * i
        else:
            break


n = int(input())

for i in gen_squared(n):
    print(i, end=" ")
