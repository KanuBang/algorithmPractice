import sys
from collections import deque

input = sys.stdin.readline

#행, 열
m,n = map(int,input().split())
graph = [list(map(int, input().rstrip())) for i in range(m)]
starts = [(0,i) for i in range(n) if graph[0][i] == 0]

def bfs(graph,v,m_max,n_max):
    m,n = v
    q = deque([(m,n)])
    graph[m][n] = 1

    dm,dn = [-1,1,0,0],[0,0,-1,1]

    while q:
        m,n = q.popleft()
        for i in range(4):
            nm, nn = m+dm[i], n+dn[i]

            if nm == m_max:
                print("YES")
                exit()

            if nm < 0 or nn < 0 or nn >= n_max or graph[nm][nn] == 1:
                continue

            q.append((nm,nn))
            graph[nm][nn] = 1

m_max = len(graph)
n_max = len(graph[0])

[bfs(graph,v,m_max,n_max) for v in starts]

print("NO")