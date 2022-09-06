s = input()
new_s = ""

for i in s:
    if i == "1":
        new_s += "one"
    else:
        new_s += i

print(new_s)