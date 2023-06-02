import sys
input = sys.stdin.readline
n = int(input())

empty = 0
star = 9

for i in range(0, n*2-1):
    print(" " * empty + "*" * star, end="")

    if i < n-1:
        empty += 1
        star -= 2
    else:
        empty -= 1
        star += 2
    
    if i != n*2-1:
        print(" ")
    else:
        print("")