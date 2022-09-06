s = input()
s_new = ""

for i, k in enumerate(s):
    if i != len(s) - 1:
        s_new += k + "*"
    else:
        s_new += k

print(s_new)