import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
nodes = [n for n in range(1,n+1)]


for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs (graph,i,visited):
    visited[i] = True
    for k in graph[i]:
        if not visited[k]:
            dfs(graph, k ,visited)

cnt = 0
for k in nodes:
    if visited[k] == True:
        continue
    dfs(graph,k,visited)
    cnt += 1
    
print(cnt)
# is와 ==의 차이점 stack is not []
