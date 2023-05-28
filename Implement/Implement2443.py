import sys

input = sys.stdin.readline
n = int(input())
empty  = 0
stars = n * 2 - 1

for i in range(0,n):
    print( " "* empty + "*" * stars + " ")
    empty += 1
    stars -= 2
