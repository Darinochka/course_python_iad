x = int(input())
q_even = 0

while x != 0:           # input to zero
    if x % 2 == 0:
        q_even += 1
    x = int(input())

print(q_even)
