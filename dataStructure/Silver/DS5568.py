'''
4
2
1
2
12
1


11, 12, 21, 112, 121, 122, 212 => 7

1/2 1/12 1/1
2/1 2/12 2/1
12/1 12/2 12/1
1/1 1/2 1/12


4C2
 1이상 99이하의 정수가 적혀져 있다. 상근이는 이 카드 중에서 k(2 ≤ k ≤ 4)장
 99C4

 376만 => n으로 짜야함
아아아아아 잘못 읽음

 n(4 ≤ n ≤ 10)장
 10C4 = 10*9*8*7 / 24 = 210 => 이론상 n^3도 가능

1
2
12
1

1. 일단 조합해서 myDict의 키로 이용
2. 그리고 생성 과정중 원래 있는 key일 경우 += 1
3. key의 개수를 출력
'''

import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
myDict = dict()
tars = []
for i in range(n):
    tars.append(input().strip())

