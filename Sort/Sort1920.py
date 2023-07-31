'''
5
4 1 5 2 3
5
1 3 7 9 5

1
1
0
0
1

1 초	128 MB

(1 ≤ N ≤ 100,000) 이중 루프 안됨

1. 일단 받는게 필요하겠지
'''

import sys
input = sys.stdin.readline

n = int(input())
comparedObj = sorted([* map(int, input().split())])
m = int(input())
subjectObj = [* map(int, input().split())]
ans =[]

for i in subjectObj:
    start = 0
    end = n-1
    while True:
        mid = 0 if start == 0 and end == 0 else (start+end) // 2
        
        if comparedObj[mid] == i:
            ans.append(1)
            break
        else:
            if i < comparedObj[mid]:
                end = mid - 1
            else:
                start = mid + 1

            if start > end:
                ans.append(0)
                break

[print(i) for i in ans]
