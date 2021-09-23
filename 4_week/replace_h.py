s = input()
new_s = ""

for i in range(len(s)):
    if (s[i] == "h" and
            s.find("h") != i and 
            s.rfind("h") != i):
        new_s += "H"
    else:
        new_s += s[i]

print(new_s)

