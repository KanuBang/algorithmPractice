'''
1 초	128 MB

Ni(1 ≤ Ni ≤ 10, i = 1, 2, ..., 5) 이 정도 범위라서 시공간 제약은 거의 없다고 본다
'''
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    myList = list(map(int, input().split()))
    sortedArr = sorted(myList,key = lambda x: x, reverse=False)
    if max(sortedArr[1:4]) - min(sortedArr[1:4]) >= 4:
        print("KIN")
    else:
        print(sum(sortedArr[1:4]))