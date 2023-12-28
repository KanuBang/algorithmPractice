import sys
input = sys.stdin.readline

node = int(input())
start, end = map(int, input().split())
visited = [False] * (node+1)
graph = [[] for _ in range(node+1)]

for _ in range(int(input())):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[u].sort()
    graph[v].append(u)
    graph[v].sort()

distance = 0
def dfs(graph, i, visited,end):
    visited[i] = True
    global distance

    for j in graph[i]:

        if not visited[j]:
            distance += 1

            if j == end:
                print(distance)
                exit()

            dfs(graph,j,visited,end)
    
    distance -= 1

dfs(graph,start,visited,end)
print(-1)