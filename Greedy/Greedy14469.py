'''
2 초	512 MB
첫 줄에 100 이하의 양의 정수 N이 주어진다. 
다음 N줄에는 한 줄에 하나씩 소의 도착 시각과 검문 시간이 주어진다. 각각 1,000,000 이하의 양의 정수이다.

3
2 1
8 3
5 7

3
2 1 
5 7
8 3
'''
'''
1 2(1번 도착) 3(1번 검문 완료) 4 5(2번 도착) 6 7 8(3번 도착) 9 10 11 12(2번 검문 완료) 13 14 15(3번 검문 완료)

2+1=3

3 < 5

5+7 = 12

12 > 8

12+3 = 15
'''

import sys
input = sys.stdin.readline
n = int(input())
myDict = dict()
total = 0
for i in range(n):
    arrive,term = map(int,input().split())
    myDict[arrive] = term

sortedDict = sorted(myDict.items(), key = lambda x : x[0])

for i in sortedDict:
    if total <= i[0]:
        total = sum(i)
    else:
        total += i[1]
print(total)

'''
1(1번 도착) 2(1번 완료, 2번 도착) 
3
2 1
5 7
8 3

8 + 
'''
