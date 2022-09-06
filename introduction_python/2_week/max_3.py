# def max_3(a, b, c):
#     if a > b:
#         if a > c:
#             return a
#     else:
#         if b > c:
#             return b
#     return c


# a = int(input())
# b = int(input())
# c = int(input())

# print(max_3(a, b, c))

a, b, c = int(input()), int(input()), int(input())

print(sorted([a, b, c])[2])
    
