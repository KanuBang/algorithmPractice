import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    graph[i].append(int(input()))

def dfs(graph, i, visited, depth):
    visited[i] = True

    for v in graph[i]:
        if not visited[v]:
            depth = dfs(graph,v,visited, depth+1)

    return depth

ans = [0]
for i in range(1, n+1):
    visited = [False] * (n+1)
    ans.append(dfs(graph,i,visited, 0))

max_v = max(ans)

for i in range(1,n+1):
    if ans[i] == max_v:
        print(i)
        exit()