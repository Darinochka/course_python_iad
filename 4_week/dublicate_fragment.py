s = input()

first = s.find("h")
second = s.rfind("h")

fragment = s[first+1:second]

print(s[:second] + fragment + s[second:])
