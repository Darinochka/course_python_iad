def q_g(w):
    q = 0
    z = ["a", "e", "i", "o", "u"]
    for i in w:
        if i in z:
            q += 1
    return q

n = int(input())

words = []

for i in range(n):
    w = input()
    words.append(w)

words = sorted(words, key=lambda x: (-q_g(x), len(x)))
print(*words, sep='\n')