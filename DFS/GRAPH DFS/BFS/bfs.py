from collections import deque

def bfs(graph, start, visited):
    #  큐 구현을 위해 deque라이브러리를 사용한다
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력 (선입선출)
        v = queue.popleft()
        print(v, end =" ")
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들에 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
'''
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
'''

graph = [
    [],
    [2,3,5],
    [4,5],
    [5,6],
    [5,8],
    [6],
    [7,9],
    [4,5,8],
    [],
    [7,8]
]
'''
1
2
3
4
5
6
7
8
9

'''

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 10

bfs(graph, 1, visited)