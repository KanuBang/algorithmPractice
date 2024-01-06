'''
이중 루프도 좀 위험해 보이긴 함
1초, 512MB(백만 정수 리스트 4MB)

the number of cups (1 ≤ N ≤ 20).
이기 때문에 시 공간산 제약은 별로 없어 보임.
하지만, 3중 루프 시에는 당연히 문제가 될테고

문제:
red 10
10 blue
green 7
=>
blue 5
red 10
green 7
=> blue green red

'''

import sys
input = sys.stdin.readline
res = []
for i in range(int(input())):
    a,b = input().split()
    [a,b] = [a,int(b)] if b.isdigit() else [b,int(a) // 2]
    res.append([b,a])

[print(i[1]) for i in sorted(res)]

