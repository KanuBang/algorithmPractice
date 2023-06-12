import sys
input = sys.stdin.readline

val = list(map(int, input().rstrip().split()))
print(val[0]*(val[1]-1) + 1)

