import sys

input = sys.stdin.readline
sys.setrecursionlimit(3000001)

n,m = map(int,input().split())
s,e = map(int,input().split())

graph = [[] for _ in range(0,n+1)]

graph[1].append(1)
graph[n].append(n-1)


for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if i == 1 or i == n:
        graph[i].sort()
        continue
    graph[i].append(i-1)
    graph[i].append(i+1)
    graph[i].sort()

print(graph)
def bfs(graph, v, end,visited, dist, path):
    visited[v] = True
    path += 1

    print(f"end:{end}, v: {v}")
    if v == end:
        print(f"path: {path}")
        dist.append(path)
        path -= 1
        return None
    
    for i in graph[v]:
        if not visited[i]:
            bfs(graph, i, end,visited,dist,path)
    
    visited[v] = False
    path -= 1

    return None

visited = [False] * (n+1)
dist = []
bfs(graph, s, e, visited, dist, -1)
print(dist)