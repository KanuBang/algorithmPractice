'''
1 초	512 MB

3 ≤ n ≤ 100
1 ≤ 학생 이름 길이 ≤ 10

삼중 루프 안 쓴다는 가정하에 최악의 이중 루프는
최악이면 10000
정수 백만 리스트 기준 4MB니까 문제 안 됨
시간 도 10000이니까 n^2 까지는 ㄱㅊ
'''

'''
1. test = [[4,"aaa"], [9,"bbb"],[2,"ccc"],[8,"ddd"]] 꼴로 만듬

2. 튜표를 받고 후보자다 인덱스를 찾고 + 1을 함
그리고 sort 한 다음 출력한다
'''

import sys
input = sys.stdin.readline
n = int(input())
studs = [[0,i] for i in input().split()]

# 각 학생 인기도 측정
for j in range(n):
    vote = input().split()
    for i in range(n):
        if studs[i][1] in vote:
            studs[i][0] += vote.count(studs[i][1])

# 인기도 기준으로 내림차순 정렬
studs.sort(reverse=True)

# 인기도 같은 학생끼리 이름 기준으로 오름차순 정렬
for i in range(n):
    for j in range(i+1,n):
        if studs[i][0] == studs[j][0]:
            if ord(studs[i][1][0]) > ord(studs[j][1][0]):
                tmp = studs[i]
                studs[i] = studs[j]
                studs[j] = tmp
# 출력
for i in studs:
    print("%s %d" %(i[1], i[0]))



