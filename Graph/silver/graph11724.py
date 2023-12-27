import sys

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
nodes = [n for n in range(1,n+1)]
stack = []

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
stack = []
for k in nodes:
    if visited[k] == True:
        continue
    
    stack.append(k)
    visited[k] = True
    while stack != []:
        top = stack.pop()
        for i in graph[top]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True

    cnt += 1

print(cnt)
# is와 ==의 차이점 stack is not []
