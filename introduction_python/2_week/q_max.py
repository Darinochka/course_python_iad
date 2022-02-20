x = int(input())
sequence = []

while x != 0:           # input to zero
    sequence.append(x)
    x = int(input())

max_num = 0
q = 0

for i in sequence:
    if max_num < i:
        max_num = i

for i in sequence:
    if i == max_num:
        q += 1

print(q)
