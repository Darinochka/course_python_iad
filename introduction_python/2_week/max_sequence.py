sequence = []

while (x := int(input())) != 0:           # input to zero
    sequence.append(x)

max_num = sequence[0]
for i in sequence:
    if max_num < i:
        max_num = i

print(max_num)
