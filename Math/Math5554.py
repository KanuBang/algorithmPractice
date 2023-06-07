import sys
input = sys.stdin.readline
listA = [int(input().rstrip()) for i in range(0,4)]
print(sum(listA) // 60) 
print(sum(listA) - 60 * (sum(listA) // 60))