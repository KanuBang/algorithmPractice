'''
3 10
10 11 13
=>12

9 1
9 5 8 1 3 2 7 6 4
=>10

첫 번째 줄에 과일의 개수 N (1 ≤ N ≤ 1,000) 과 스네이크버드의 초기 길이 정수 L (1 ≤ L ≤ 10,000) 이 주어집니다.
두 번째 줄에는 정수 h1, h2, ..., hN (1 ≤ hi ≤ 10,000) 이 주어집니다.

1 초	128 MB
'''

import sys
input = sys.stdin.readline
fruits, snake = map(int, input().split())
heights = sorted([* map(int, input().split())])

for i in heights:
    if snake >= i:
        snake += 1
    else:
        break

print(snake)
