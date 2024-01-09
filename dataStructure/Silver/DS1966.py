import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

while n > 0:

    numberOfDocs, targetIdx = map(int,input().split())
    importances = list(map(int, input().split()))
    queue = deque([[i, importances[i]] for i in range(len(importances))])
    printedOrder = 0

    while True:
        beforeSize = len(queue)
        front = queue.popleft()

        for item in queue:
            if item[1] > front[1]:
                queue.append(front)
                break
        
        nowSize = len(queue)
        
        if beforeSize != nowSize:
            printedOrder += 1
        
            if front[0] == targetIdx:
                print(printedOrder)
                break
        
    n -= 1


'''
idx:2 -> 3은 몇번째로 출력되는가?
1: [0,1] [1,2] [2,3] [3,4]
2: [1,2] [2,3] [3,4] [0,1]
3: [2,3] [3,4] [0,1] [1,2]
4: [3,4] [0,1] [1,2] [2,3] -> 4 print(popleft) (cnt = 1)
5: [0,1] [1,2] [2,3]
6: [1,2] [2,3] [0,1]
7: [2,3] [0,1] [1,2] -> 3 print(popleft) (cnt = 2) -> idx:2 break

'''