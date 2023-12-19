''' 조건
시간제한 1초, 메모리 256MB
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

최악의 경우 O(199999) 이기에 시간 복잡도는 별 문제가 없다
'''

'''
1. 정보를 입력받는다
2. 입력 받은 정보로 그래프를 만든다.
3. 
'''

'''
   1
 4  6
2 7  3
      5

'''

'''
def dfs(graph, node, visited):
    
    visitied[node] = True
    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
            dfs(graph, i, visited)

'''

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [ [] for i in range(n+1)]
visitied = [False] * (n+1)
# DFS를 이용했다면 BFS로

def bfs(graph,node, visited):
    queue = deque([node])
    visited[node] = True
    parent = [None] * (n+1)

    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                parent[i] = cur
                queue.append(i)
                visited[i] = True
    return parent


for i in range(n-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

parent = bfs(graph, 1, visitied)
[print(i) for i in parent[2:]]







