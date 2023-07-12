'''
학생의 수가 100 이하이고, 학생들이 뽑는 번호는 0 또는 자연수이며 학생들이 뽑은 번호 사이에는 빈 칸이 하나씩 있다.

시간: 1초
N의 범위가 500인 경우 ⇒ O(n3)임
범위가 100이하 이기에 넉넉해보임


공간: 128 MB

n이 100이하라서 공간은 정말 넉넉해보임.
왜냐 백만 정수 리스트여야 4MB가 정도되는데
학생 수가 100이하면 정말 남아 돔

0 1 1 3 2

'''

a = int(input().rstrip())
idxs = [*map(int, input().split())]
ans = [None]*a

for i in range(0,a):
    idx = idxs[i]
    if ans[idx] != None:
        for j in range(i-1,idx-1,-1):
            ans[j+1] = ans[j]
    ans[idx] = i+1

[print(i, end=" ") for i in reversed(ans)]