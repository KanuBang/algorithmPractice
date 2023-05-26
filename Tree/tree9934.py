'''
import sys
input = sys.stdin.readline

k = int(input()) # k - 1 = 트리의 레벨
values1 = list( map(lambda x: int(x), input().split()) )
tree = [[] for _ in range(k)]

def makeTree(arr, x):
    mid = len(arr) // 2
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], x+1)
    makeTree(arr[mid+1: ], x+1)

makeTree(values1, 0)
for i in range(k):
    print(*tree[i])
'''



import sys
input = sys.stdin.readline
k = int(input())
values = list(map(lambda x: int(x) ,input().split()))
tree = [[] for _ in range(0,k)]

'''
3
[[[1] 6 [4]] 3 5 2 7]

    3
   6 2
 1 4 5 7
'''

def makeTree(arr , x):
    mid = len(arr) // 2
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], x+1)
    makeTree(arr[mid+1:], x+1)

makeTree(values, 0)
for i in range(k):
    print(*tree[i])
    #언패킹 연산자로 행에 있는 모든 요소들에 접근한다