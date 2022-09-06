n = int(input())

ping = """
lajdfd
dfg
dfgdfg
dfg
"""

ping = ping.split("\n")

for p in ping:
    for i in range(n):
        if i != n - 1:
            print(p, end=" " * (10 - len(p)))
        else:
            print(p)
