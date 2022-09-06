n = int(input())

s = input().split()
c = n // 2

if s != s[::-1]:
    while c != n:
        c += 1
        start = c - len(s[(c+1):])
        # print(s[(c+1):] + s[:c][::-1])
        if s[:(c+1)][::-1] == s[(c+1):] + s[:c][::-1]:
            print(len(s[:c][::-1]))
            print(*s[:c][::-1])
            break
        # elif s[start:(c+1)] == s[(c + 1):][::-1]:
        #     print(s[:(start-1)][::-1])
        #     break
        elif s[start:c] == s[(c + 1):][::-1]:
            print(start)
            print(*s[:start][::-1])
            break
        
    else:
        print(*s[::-1][1:])
else:
    print(0)