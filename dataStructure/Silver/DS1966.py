import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
'''
1 0
5

idx: 0 -> 5
sort -> 5
5는 첫 번째로 인쇄

4 2
1 2 3 4
idx:2 -> 3
2 3 4 1
3 4 1 2
4 1 2 3


6 0
1 1 9 1 1 1
idx:0 -> 1a

1a 1b 9 1c 1d 1e
idx: 0 -> 1a

1b 9 1c 1d 1e 1a
9 1c 1d 1e 1a 1b


'''
while n > 0:
    numberOfDocs, target = map(int,input().split())
    queue = deque(list(dict(map(int, input().split()))))
    
    print(queue)


    n -= 1
