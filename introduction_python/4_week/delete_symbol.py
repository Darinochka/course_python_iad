s = input()
s_new = ""

for i in s:
    if i != "@":
        s_new += i

print(s_new)