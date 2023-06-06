import sys
input = sys.stdin.readline
k = input().rstrip()
a = list(map(int, k.split(' ')))
a.sort()
for i in a:
    print(i, end=" ")