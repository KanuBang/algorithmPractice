import sys
from collections import deque

input = sys.stdin.readline

def bfs (start_x, start_y):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    queue = deque()
    queue.append((start_x,start_y))
    while queue:
        x,y = queue.popleft()
        #y,x = queue.popleft() 오류의 원인?
        #print(x,y)
        graph[y][x] = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (nx < 0 or ny < 0 or nx >= m or ny >= n) or graph[ny][nx] == 0:
                continue
            
            if graph[ny][nx] == 1:
                queue.append((nx,ny))


ans = [ ]
for i in range(int(input())):
    # 가로 m, 세로 n 만약 10, 8이면 가로10 세로8
    m,n,k = map(int, input().split())
    # row = [0] * m -> 깊은복사, 얕은 복사 문제
    graph = [[0] * m for _ in range(n)]
    cabbage_locations = []
    cnt = 0
    for a in range(k):
        x,y = map(int, input().split()) # 4,2 -> 4 가로, 2 세로
        cabbage_locations.append((x,y)) # x 가로, y 세로
        graph[y][x] = 1
   
    #[print(graph[i]) for i in range(n)]
    #print("111")
    for (x,y) in cabbage_locations:
        if graph[y][x] == 1:
            #print(f"y:{y}, x:{x}, value: {graph[y][x]}")
            bfs(x,y)
            cnt += 1
        
        #else
        #print(f"y:{y}, x:{x}, value: {graph[y][x]}")
        
    #ans.append(cnt)
    print(cnt)
    
    


                

