import sys
from collections import deque

input = sys.stdin.readlineㅅd 

# 도시의 개수, 도로의 개수, 거리, 시작 정점
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
nodes_dist = [0] * (n+1)

for i in range(m):
    u,v= map(int, input().split())
    graph[u].append(v)
    graph[u].sort()

def bfs(graph, s, visited):
    queue = deque([s])
    visited[s] = True

    while queue:
        previous_node = queue.popleft()
        for node in graph[previous_node]:
            if not visited[node]:
                queue.append(node)
                nodes_dist[node] = nodes_dist[previous_node] + 1
                visited[node] = True
        
        
bfs(graph,x,visited)

ans = [idx for idx in range(1, n+1) if nodes_dist[idx] == k]

if ans:
    print(*ans, sep='\n')
else:
    print(-1)


'''
sign = True

for idx in range(1, n+1):
    if nodes_dist[idx] == k:
        print(idx)
        sign = False

if sign == True:
    print(-1)
    '''
        