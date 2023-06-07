import sys
input = sys.stdin.readline
print(min([int(input().rstrip()) for i in range(0,3)]) + min([int(input().rstrip()) for i in range(0,2)]) - 50)