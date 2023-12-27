import sys
from collections import deque

input = sys.stdin.readline

def bfs(len_w, len_h, graph):
    queue = deque()
    # 상,하,좌,우 + 왼쪽 위 대각선, 왼쪽 아래 대각선, 오른쪽 위 대각선, 오른쪽 아래 대각선
    dh = [-1,1,0,0] + [-1,1,-1,1]
    dw = [0,0,-1,1] + [-1,-1,1,1]
    land = 0
    for i in range(len_h):
        for j in range(len_w):

            if graph[i][j] == 1:
                land += 1
                queue = deque()
                queue.append((j,i)) # w,h
                while queue:
                    w,h = queue.popleft()
                    for k in range(8):
                        nh = h + dh[k]
                        nw = w + dw[k]
                        
                        if nw < 0 or nh < 0 or nw >= len_w or nh >= len_h:
                            continue

                        if graph[nh][nw] == 0:
                            continue
                        
                        queue.append((nw,nh))
                        graph[nh][nw] = 0

    return land

while True:
    w,h = map(int, input().split())
    graph = []
    if w == 0 and h == 0:
        break

    for i in range(h):
        graph.append(list(map(int, input().split())))
    print(bfs(w,h,graph))