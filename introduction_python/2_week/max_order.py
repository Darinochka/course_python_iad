x = int(input())
sequence = []

while x != 0:
    sequence.append(x)
    x = int(input())

q = 1
max_q = 1
curr = 0

for x in sequence:
    if x == curr:
        q += 1
    else:
        if max_q < q:
            max_q = q
        q = 1
    curr = x
else:
    if max_q < q:
        max_q = q
print(max_q)
