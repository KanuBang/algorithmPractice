import sys
from collections import deque

input = sys.stdin.readline

def bfs (start_x, start_y):
    queue = deque()
    queue.append((start_x,start_y))
    graph[start_y][start_x] = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ny,nx = y + dy[i], x + dx[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[ny][nx] == 0:
                continue
            
            queue.append((nx,ny))
            graph[ny][nx] = 0

ans = [ ]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for i in range(int(input())):

    m,n,k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cabbage_locations = []
    cnt = 0
    
    for a in range(k):
        x,y = map(int, input().split()) 
        graph[y][x] = 1
        cabbage_locations.append((x,y)) 
    
    for (x,y) in cabbage_locations:
        if graph[y][x] == 1:
            bfs(x,y)
            cnt += 1
    print(cnt)

''' 오류 원인
1. 가로, 세로 혼동
2. row = [0] * m -> 깊은복사, 얕은 복사 문제
3. 방문 처리 미흡으로 인한 queue에 중복 좌표 포함 문제 -> 메모리 초과, 시간 초과
'''
    
'''
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 1, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
deque([(1, 0)])
deque([(1, 1)])
deque([])
deque([(4, 3)])
deque([])
deque([])
deque([(3, 4)])
deque([])
deque([(7, 5), (8, 4)])
deque([(8, 4), (7, 6), (8, 5)])
deque([(7, 6), (8, 5), (8, 5), (9, 4)])
deque([(8, 5), (8, 5), (9, 4), (8, 6)])
deque([(8, 5), (9, 4), (8, 6), (8, 6), (9, 5)])
deque([(9, 4), (8, 6), (8, 6), (9, 5), (8, 6), (9, 5)])
deque([(8, 6), (8, 6), (9, 5), (8, 6), (9, 5), (9, 5)])
deque([(8, 6), (9, 5), (8, 6), (9, 5), (9, 5), (9, 6)])
deque([(9, 5), (8, 6), (9, 5), (9, 5), (9, 6), (9, 6)])
deque([(8, 6), (9, 5), (9, 5), (9, 6), (9, 6), (9, 6)])
deque([(9, 5), (9, 5), (9, 6), (9, 6), (9, 6), (9, 6)])
deque([(9, 5), (9, 6), (9, 6), (9, 6), (9, 6), (9, 6)])
deque([(9, 6), (9, 6), (9, 6), (9, 6), (9, 6), (9, 6)])
deque([(9, 6), (9, 6), (9, 6), (9, 6), (9, 6)])
deque([(9, 6), (9, 6), (9, 6), (9, 6)])
deque([(9, 6), (9, 6), (9, 6)])
deque([(9, 6), (9, 6)])
deque([(9, 6)])
deque([])
5
    
    '''
    


                

