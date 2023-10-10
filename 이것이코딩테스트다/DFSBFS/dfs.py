# DFS 메서드 정의
cntE = 0
cntV = 0
def dfs(graph, v, visited):  
    global cntE
    global cntV
    cntV += 1  
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 인접한 노드 중에서 방문하지 않은 노드가 있다면 그 노드를 탐색한다.
    for i in graph[v]:
        cntE += 1
        if not visited[i]:
            dfs(graph,i,visited)

            
# 1(1->2). 2(2->1), 3(2->7), 4()
# 인접 리스트로 그래프 표현
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현한다(1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
print(cntV + cntE)
