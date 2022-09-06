s = input()
s_new = ""

for i, k in enumerate(s):
    if i % 3 != 0:
        s_new += k

print(s_new)