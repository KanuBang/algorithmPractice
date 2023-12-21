from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int, map(int, input().split()))

# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 미로 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

# 미로 탐색
def bfs_maze(x,y):
    queue = deque()
    queue.append((x,y))

    # queue가 empty가 될때까지 반복한다.
    while queue:
        #현재 좌표
        x,y = queue.popleft()

        #현재 좌표에서 상,하,좌,우로 움직인다.
        for i in range(4):
            # 다음 좌표
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 다음 좌표가 미로를 벗어난다면 pass
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 다음 좌표가 벽(0)이라면 pass
            if graph[nx][ny] == 0:
                continue
            
            # 다음 좌표가 벽(1)이라면 다음 좌표의 값을 현재 좌표의 값 + 1로 설정한다.
            # graph의 요소 value는 0,0 시작으로부터 그 좌표까지 이동 거리를 의미한다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    # 최종 이동 거리를 반환한다.
    return graph[n-1][m-1]

print(bfs_maze(0,0))# 미로 탐색 호출