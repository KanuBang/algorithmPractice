''' 제한
시간: 5초
메모리: 256
N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, 
"A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

100000 * 100000 / 
'''

'''
5 4
3 1
3 2
4 3
5 3

3->1
3->2
4->3
5->3

1 2
 3
4 5
'''

'''
1. 그래프를 만든다. 이 문제는 방향 그래프으로 만들어야 될 거 같다.
2. bfs 탐색을 한다.
3. 시작 노드를 1~5 일때 탐색할 수 있는 노드가 몇개 이냐 해킹할 수 있는 컴터의 개수이다.
4. 3번의 정보를 리스트에 담고 max를 찾은 다음 그 max 에 해당하는 인덱스를 따로 ans에 저장한다.
4. 오름차순으로 정렬 후 출력한다.
'''
import sys 
from collections import deque

# 정보를 받아 방향 그래프 graph를 생성한다.
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)

# bfs 탐색
def bfs(graph,v):
    visited = [False] * (n+1)    
    infect = 0 # 감염된 컴퓨터의 수
    queue = deque([v])
    visited[v] = True

    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                infect += 1 # 탐색됨 = 감염됨 -> 감염 + 1
    
    return infect # 시작 노드가 x일 때, 감염된 컴퓨터의 수

# 시작 노드가 인덱스 i일 때 감염된 컴퓨터의 수
cnt = [bfs(graph,i) for i in range(1, n+1)]
cnt_max = max(cnt)
# 정답 출력
[print((i+1), end=" ") for i in range(0,n) if cnt_max == cnt[i]]
