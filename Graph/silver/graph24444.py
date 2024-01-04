import sys
from collections import deque

input = sys.stdin.readline
m,n,r = map(int,input().split())
graph = [[] for _ in range(m+1)]

for i in range(n):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

[graph[i].sort() for i in range(1,m+1)]

def bfs(graph, i, visited,ans):
    queue = deque([i])
    visited[i] = True
    cnt = 0
    while queue:
        cnt += 1
        v = queue.popleft()
        ans[v] = cnt

        for r in graph[v]:
            if not visited[r]:
                queue.append(r)
                visited[r] = True
    
visited = [False] * (m+1)
ans = [0] * (m+1)
bfs(graph,r,visited,ans)
[print(ans[k]) for k in range(1,m+1)]

