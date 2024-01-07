import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

queue = deque()
def isEmpty(queue):
    return not queue

while n > 0:
    command = input().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    
    elif command[0] == 'size':
        print(len(queue))
    
    elif command[0] == 'empty':
        print(1) if isEmpty(queue) else print(0)

    elif command[0] == 'pop':
        print(-1) if isEmpty(queue) else print(queue.popleft())

    elif command[0] == 'front':
        print(-1) if isEmpty(queue) else print(queue[0])

    elif command[0] == 'back':
        print(-1) if isEmpty(queue) else print(queue[-1])

    n -= 1