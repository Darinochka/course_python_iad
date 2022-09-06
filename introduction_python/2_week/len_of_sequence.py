x = int(input())
q = 0

# ---------- FIRST OPTION ------------
while x != 0:           # input to zero
    q += 1
    x = int(input())

# ---------- SECOND OPTION -------------
# while (x := int(input())) != 0:
#     q += 1

print(q)
