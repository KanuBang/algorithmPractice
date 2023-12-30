import sys
from collections import deque

input = sys.stdin.readline
m,n = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(m)]

def bfs(graph,y,x):

    if graph[y][x] == '-':
        graph[y][x] = 0
        dx = x

        while dx < n:
            dx += 1

            if dx >= n:
                break

            if graph[y][dx] =='|' or graph[y][dx] ==0:
                break

            graph[y][dx] = 0
    
    else:
        graph[y][x] = 0
        dy = y

        while dy < m:
            dy += 1

            if dy >= m:
                break

            if graph[dy][x] =='-' or graph[dy][x] ==0:
                break

            graph[dy][x] = 0
            
    return 1


cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] != 0:
            cnt += bfs(graph, i, j)

print(cnt)