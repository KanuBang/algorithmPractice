''' 제한
1초, 256MB
지도 크기 최대 25*25 -> 시간 제한은 까다롭지 않음
'''
from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip())))


def dfs(x,y):
    global cnt

    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    
    return False

result = 0
ans = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i,j) == True:
            result += 1
            ans.append(cnt)

print(result)
[print(i) for i in sorted(ans)]