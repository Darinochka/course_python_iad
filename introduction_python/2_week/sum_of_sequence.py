x = int(input())
sum_nums = 0
q = 0

while x != 0:           # input to zero
    sum_nums += x
    q += 1
    x = int(input())

# while (x := int(input())) != 0:
#     sum_nums += x

print(sum_nums)
