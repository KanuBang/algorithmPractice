'''
2초, 256MB

T: 테스트 테이스
N: 정수의 개수 1 <=  N <= 1000000
M: 수첩에 적혀있는 정수의 개수 1 <= M <= 1000000

수첩2에 적혀있는 M개의 숫자 순서대로, 수첩 1에 있으면 1, 없으면 0을 출력한다.

최악 O(T*N*M)이면 시간 초과
O(T* (N+M) )이 이상적
'''

import sys
input = sys.stdin.readline

t = int(input())
note1 = []
for i in range(t):
    
    n = int(input())
    note1 = list(map(int, input().split()))

    m = int(input())
    note2 = list(map(int, input().split()))

    for k in note2:
        if k in note1:
            print(1)
            continue
        print(0)
    

