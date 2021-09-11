n = int(input())

ping = """
   _~_
  (o o)
 /  V  \\
/(  _  )\\
  ^^ ^^
"""

ping = ping.split("\n")[1:-1]

for p in ping:
    for i in range(n):
        if i != n - 1:
            print(p, end=" " * (10 - len(p)))
        else:
            print(p)
