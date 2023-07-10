'''
공간:128MB
int리스트 기분 3천2백만 개 수용 가능

5 20
99 101 1000 0 97

-1 1 900 -100 -3

'''
'''
1m2당 5명
공간 20m2
산긍이의 확신: 100명

신문기사


1. 입력 받자 마자 상근이의 확신을 구함
2. 그리고 입력받으면서 확신을 뺌
3. 그리고 출력
'''

inf = list(map(int,input().split()))
num = inf[0] * inf[1]
news = list(map(int,input().split()))
for i in news:
    print(i - num, end = " ")
