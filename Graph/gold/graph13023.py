import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
'''
5 5
0 1
1 3
1 4
4 3
3 2
'''
n,m = map(int, input().split())
nodes = [n for n in range(n)]
graph = [[] for _ in range(n)]

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[u].sort()
    graph[v].append(u)
    graph[v].sort()


def dfs(graph, i, visited, route):
    visited[i] = True
    route.append(i)
    #print(f"r: {route}")
    if len(route) == 5:
        print(1)
        exit()


    for j in graph[i]:
        if not visited[j]:
            dfs(graph,j,visited,route)
    
    visited[route.pop()] = False

    return route


for i in nodes:
    visited = [None] * (n)
    dfs(graph,i,visited, [])

print(0)
    
    


