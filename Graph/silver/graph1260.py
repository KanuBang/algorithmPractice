''' 조건
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 
간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
시간제한 2초
메모리 제한 128MB

파이썬 1초에 2000만번 연산 가능하다. 
그래프 탐색 알고리즘의 시간 복잡도는 O(V+E)의 최대치는 11000이다.
시간 복잡도는 문제 없다. 
'''
''' 알고리즘

간단한 그래프 탐색 문제이다.

1. 그래프 정보를 입력받아 저장한다.
2. 입력 받은 정보를 토대로 그래프를 생성한다. 이때, 노드는 오름차순으로 정렬되어야 한다.
3. 그래프 탐색을 각각의 방식으로 시도한다.
4. 그래프 탐색을 하면서 방문 노드를 출력한다.
'''
from collections import deque
# 1. 그래프의 정보를 입력받아 저장한다.
node, edge, start = map(int,input().split())
graph = [[] for i in range(node+1)]

for i in range(edge):
    inp = list(map(int, input().split()))
    graph[inp[0]].append(inp[1])
    graph[inp[1]].append(inp[0])
    graph[inp[0]].sort() # 낮은 숫자 우선 방문을 위한 오름차순 정렬
    graph[inp[1]].sort()

# dfs, bfs 함수
def dfs(graph, v, visit):
    visit[v] = True
    print(v, end =" ")
    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

# 방문테이블동시에 사용시 리셋 필요
def bfs(graph, v, visit):
    queue = deque([v])
    visit[v] = True
    while queue:
        tar = queue.popleft()
        print(tar, end =" ")
        for i in graph[tar]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True
    

visit = [False] * (node+1)
dfs(graph,start, visit)
visit = [False] * (node+1)
print()
bfs(graph,start,visit)

    
