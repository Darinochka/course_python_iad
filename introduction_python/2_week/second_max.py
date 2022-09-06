sequence = []

while (x := int(input())) != 0:           # input to zero
    sequence.append(x)

max_num = 0
max_second = 0

for i in sequence:
    if max_num <= i:
        max_second, max_num = max_num, i
    elif max_second < i:
        max_second = i

print(max_second)
