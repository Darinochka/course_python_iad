def gen_squared(n):
    for i in range(1, n+1):
        yield i * i


n = int(input())
sum_square = 0

# ------------------FIRST OPTION----------------------
# for i in gen_squared(n):
#     sum_square += i

# ------------------SECOND OPTION----------------------
# sum_square = sum([i * i for i in range(1, n+1)])

# ------------------THIRD OPTION-----------------------
# sum_square = sum(gen_squared(n))

# -------------------FOURTH OPTION----------------------
partial_sum = [sum_square := sum_square + i for i in gen_squared(n)]

print(partial_sum)
