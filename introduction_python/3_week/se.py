x = int(input())
s = []

while x != 0:           # input to zero
    s.append(x)
    x = int(input())

avg = sum(s) / len(s)
se = 0
for i in s:
    se += (i - avg) ** 2

se = (se/(len(s)-1)) ** (1/2)

print(se)