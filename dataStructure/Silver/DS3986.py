'''
첫째 줄에 단어의 수 N이 주어진다. (1 ≤ N ≤ 100)
다음 N개 줄에는 A와 B로만 이루어진 단어가 한 줄에 하나씩 주어진다. 
단어의 길이는 2와 100,000사이이며, 모든 단어 길이의 합은 1,000,000을 넘지 않는다.

100 * 100000 = 10000000

n^2이 적당해보인다...
'''

import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(n):

    word = list(input().rstrip())
    stack = []

    for j in range(len(word)):
        current = word.pop()

        if stack == []:
            stack.append(current)

        elif stack[-1] == current:
            stack.pop()

        else:
            stack.append(current)

    if stack == []:
        cnt += 1

print(cnt)



