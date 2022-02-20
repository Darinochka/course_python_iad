from math import sqrt


def check_square():
    key = False

    def print_square(n):
        if n != 0:           # input to zero
            print_square(int(input()))
            if sqrt(n) == int(sqrt(n)):
                print(n, end=" ")
                global key
                key = True
        else:
            pass
    
    print_square(int(input()))
    if not key:
        print(0)