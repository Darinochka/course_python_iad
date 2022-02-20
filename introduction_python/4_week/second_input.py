s = input()

first = s.find("f")
second = s[first+1:].find("f") if first > -1 else -1

if second != -1:
    print(second + first + 1)
elif first != -1:
    print(-1)
else:
    print(-2)