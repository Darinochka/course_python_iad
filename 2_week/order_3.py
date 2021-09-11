a, b, c = int(input()), int(input()), int(input())


if a > b:
    if b > c:               # a b c
        a, c = c, a         # c b a
    elif a > c:             # a c b
        a, b, c = b, c, a
    else:                   # c a b
        a, b, c = b, a, c
else:                       # b a
    if a > c:               # b a c
        a, b, c = c, a, b 
    elif c > b:             # c b a
        pass                # a b c
    else:                   # b c a
        b, c = c, b         # a c b
        
print(a, b, c)
