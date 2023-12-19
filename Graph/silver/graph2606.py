''' 설계
시간 제한	메모리 제한	제출
1 초	128 MB

첫째 줄에는 컴퓨터의 수가 주어진다. 
컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

시간복잡도 공간복잡도는 딱히 문제가 없어보인다.
!!!!천만 1초!!!1

# 1.입력을 받고 그래프를 만들다
# 2.그래프를 탐색한다. DFS / BFS -> 1, 2, 3, 5, 6 순이 간접 언급되어 있으므로 DFS로 탐색하겠다
# 3. 1번 컴퓨터로부터 감염된 컴퓨터 개수를 출력한다.
'''

'''
1차 수정: 그래프 표현이 무방향 그래프 특성을 반영하지 못해 다시 코딩함
-> 해결
'''

# dfs 탐색
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
   

n = int(input()) + 1 # 컴퓨터의 수 (+1을 한 이유는 컴퓨터1을 인덱스1과 매칭시키기 위함이다.)
c = int(input()) # 쌍 개수
graph = [[] for i in range(n)] # 그래프

# 그래프 생성(무방향 그래프)
for i in range(c):
    inp = list(map(int, input().split()))
    graph[inp[0]].append(inp[1])
    graph[inp[1]].append(inp[0])


# 방문기록테이블
visited = [False] * n

# 호출
dfs(graph,1,visited)

# 1번으로부터 감염된 컴퓨터 개수 출력, True는 감염
print(visited[2:len(visited)].count(True))



