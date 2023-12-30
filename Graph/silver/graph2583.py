import sys
from collections import deque

input = sys.stdin.readline

m,n,k = map(int,input().split())

graph = [[0] * n for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int, input().split()) # x1<x2

    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1 # 1=영역

graph = list(reversed(graph))


def bfs(graph, col, row):
    queue = deque()
    queue.append((col, row))
    graph[col][row] = 1
    size = 0
    while queue:
        col,row = queue.popleft()
        size += 1
        dcol = [-1,1,0,0]
        drow = [0,0,-1,1]
        for v in range(4):
            ncol = col + dcol[v]
            nrow = row + drow[v]

            if ncol < 0 or nrow < 0 or ncol >= m or nrow >= n:
                continue

            if graph[ncol][nrow] == 1:
                continue
            
            graph[ncol][nrow] = 1
            queue.append((ncol,nrow))
    
    return size

areas = []
for col in range(m):
    for row in range(n):
        if graph[col][row] == 0:
            areas.append(bfs(graph,col,row))

areas.sort()
print(len(areas))
[print(item, end= " ") for item in areas]