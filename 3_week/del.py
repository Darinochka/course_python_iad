a, b = int(input()), int(input())

d = (a+b-1)//b-(a//b)
print("YES"*(1-d) + "NO"*d)