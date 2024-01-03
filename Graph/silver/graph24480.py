import sys
from collections import deque

sys.setrecursionlimit(2500)
input = sys.stdin.readline
m,n,r = map(int,input().split())
graph = [[] for _ in range(m+1)]

for i in range(n):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

[graph[i].sort(reverse=True) for i in range(1,m+1)]

cnt = 0
def dfs(graph, i, visited):
    global cnt
    cnt += 1
    visited[i] = True
    ans[i] = cnt
    for v in graph[i]:
        if not visited[v]:
            dfs(graph, v, visited)
    return None


visited = [False] * (m+1)
ans = [0] * (m+1)
dfs(graph, r, visited)
[print(ans[i]) for i in range(1, m+1)]

