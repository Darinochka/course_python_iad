x = int(input())
sequence = []

while x != 0:           # input to zero
    sequence.append(x)
    x = int(input())

q_max = 0
q = 0
key = False

for i in range(1, len(sequence)):

    if sequence[i-1] < sequence[i]:
        if not key:
            q = 0
        key = True
        q += 1

    elif sequence[i-1] > sequence[i]:
        if key:
            q = 0
        key = False
        q += 1
    
    if q_max < q:
        q_max = q

    if sequence[i-1] == sequence[i]:
        q = 0

print(q_max+1)
