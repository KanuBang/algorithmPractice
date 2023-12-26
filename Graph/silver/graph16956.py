import sys

input = sys.stdin.readline
r,c = map(int, input().split()) 
graph = []

for i in range(r):
    graph.append(list(input().rstrip()))

dx = [-1,1,0,0] 
dy = [0,0,-1,1]
sheep,wolf,empty,defence = ('S','W','.','D') # 가독성

for i in range(r):
    for j in range(c):
        if graph[i][j] == wolf:
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue
                
                if graph[nx][ny] == sheep:
                    print(0)
                    exit()
            continue

        if graph[i][j] == sheep or graph[i][j] == defence:
            continue

        graph[i][j] = defence

print(1)
[print(''.join(i)) for i in graph]

'''
def bfs(start_x,start_y):
    queue = deque()
    queue.append((start_x,start_y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + row[i]
            ny = y + col[i]

            if nx < 0 or ny < 0 or nx >=r or ny >= c:
                continue
                
            if graph[nx][ny] == wolf or graph[nx][ny] == sheep:   
                graph[x][y] = defence
                continue
            
            if graph[nx][ny] == defence:
                continue

            if graph[nx][ny] == empty:
                graph[x][y] = defence
                queue.append((nx,ny))

bfs(0,0)
[print(''.join(i)) for i in graph]
'''

