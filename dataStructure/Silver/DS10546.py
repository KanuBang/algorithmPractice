'''
베부른 마라토너

참가자: 100000
완주자: 99999

remove의 시간 복잡도는 N
dictionary pop은 같은 key값은 모조리 삭제하는 건가? 
'''

import sys

input = sys.stdin.readline
n = int(input())
challengers = {}

#참가자 이름
for i in range(n):
    name = input().rstrip()
    if name in challengers:
        challengers[name] += 1
    else:
        challengers[name] = 1

#완주자 이름
for i in range(n-1):
    name = input().rstrip()
    if challengers[name] == 1:
        challengers.pop(name)
    else:
        challengers[name] -=1

print(*challengers)
