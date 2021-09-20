x = int(input())
sequence = []

while x != 0:           # input to zero
    sequence.append(x)
    x = int(input())

q = 0
for i in range(1, len(sequence)):
    if sequence[i-1] < sequence[i]:
        q += 1

print(q)