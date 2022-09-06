x = int(input())
s = []

while x != 0:           # input to zero
    s.append(x)
    x = int(input())

idx = [x for x in range(1, len(s) - 1) if s[x-1] < s[x] and s[x] > s[x+1]]
print(idx)
print(min(map(lambda x: idx[x] - idx[x-1], range(1, len(idx)))) if len(idx) > 1 else 0)
