import sys

input = sys.stdin.readline
n = int(input())
empty = n-1 #4
star = 1 #1

for i in range(0, n*2):
    print(" " * empty + "*" * star + " ")
    
    if i < n-1:
        empty -= 1
        star += 2
    else:
        empty += 1
        star -= 2
