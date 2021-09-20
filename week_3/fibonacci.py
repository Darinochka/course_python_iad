n = int(input())

prev_f = 1
next_f = 0
i = 0

while next_f != n:
    temp = next_f
    next_f = temp + prev_f
    prev_f = temp
    i += 1
    if next_f > n:
        print(-1)
        break
else:
    print(i)
