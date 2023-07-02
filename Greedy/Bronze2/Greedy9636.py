'''
시간: 1초
(1 ≤ T ≤ 100) => 빅오의 n^3 해도 별문제 없을 가능성 높음

공간: 128MB
백만 정수 리스트 4MB
백만 * 32 =>3천2백만 => 좀 적네

For each test case, 
print a single line which contains 4 integers separated by a single space, 
which are the minimum possible X-coordinate, the minimum possible Y-coordinate, 
the maximum possible X-coordinate and the maximum possible Y-coordinate for the location of the robot after it stopped moving.

RUL?R?D

(1,0)

최소 x => L => RULLRLD
(1,0)
(1,1)
(0,
최소 y => D
최대 x => R
최대 y => U


-1 -2 3 2

설계
1. 문자를 읽고
2. ?을 제외하고 좌표를 구한다
3. ?이 몇개인지 구한다
4. ?개수를 기반하여 최소, 최대 x,y를 만든다
'''

import time
start = time.time()

import sys
input = sys.stdin.readline
n = int(input())
#s = [ input().rstrip() for i in range(n)]

for i in range(n):
    x,y,q = (0,0,0)
    s = input().rstrip()
    for j in s:
        if j == "R":
            x+= 1
        elif j == "L":
            x-= 1
        elif j == "D":
            y -= 1
        elif j == "U":
            y += 1
        else:
            q += 1

    print(x-q,y-q,x+q,y+q, end = " ")
    print()


end = time.time()