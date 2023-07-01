'''
시간:1초
N의 범위: 1000

빅오(n^2)까지 ㄱㅊ


공간:1024

정수형 리스트 백만 4Mg
백만 * 256 => 왠만해서는 문제 없을 듯..
'''

'''
N개의 사탕 묶음 (준석이는 무제한으로 구매 가능)
i 번째 사탕 묶음에는 a_i개 사탕 존재

조건
1. 사간 사탕의 총 개수가 짝수가 되어야 함
2. 최대 사탕 개수 구하기

입력
1. 사탕 묶음 = N (1 <= N <= 1000)
2. 둘째 줄에는 각각의 사탕 묶음에 담겨있는 사탕의 개수
a1, a2, ... an이 주어짐
( 1<=an<=1000)

출력
1. 최대로 가져갈 수 있는 사탕 개수
2. 사탕 개수는 홀수로만 가져갈 수 있음
'''

'''
5
8 3 6 7 5

8 + 3 = 11
11 + 6 = 17
17 + 7 = 24
24 + 5 = 29

if 총 합이 짝수
참: 답

if 총 합이 홀수


짝수 + 짝수 = 짝수
홀수 + 홀수 = 짝수

짝수 + 홀수 = 홀수

8 3 6 7 5
짝수 2개
홀수 3개


만약 다 짝수라면 => 합이 답
만약 다 홀수이면
=> 그리고 홀수가 홀수 개 이면 => 가장 작은 홀수를 뺀다
=> 홀수가 짝수 개 이면 => 합이 답

만약 홀수 + 짝수라면
=> 
2 4 => 2
3 5 7 => 3
= 홀수 + 홀수 + 홀수 => 홀수 

2 4 => 2
3 5 7 9 => 4
= 홀수 + 홀수 + 홀수 + 홀수 => 홀수 

2 4 6 => 3
3 5 7 => 3
= 홀수 + 홀수 + 홀수 => 홀수

2 4 6 => 3
3 5 => 2
=> 홀수 + 홀수 + 짝수 => 짝수
'''

'''
1. 다 더해서 합이 짝수이면 => 이게 답이다
2. 다 더해서 합이 홀수이면
2-1) 가장 작은 홀수를 뺀다
1 1 3 3 3
1 1 1 1 3
1 1 1
1

'''

'''
결론
1. 입력을 받는다
2. 만약 크기가 1이고 요소가 홀수라면 => 리턴 0 / 아니면 그대로 진행
3. 합을 구한다
4. 합이 짝수이면 => 답
5. 합이 홀수이면 합에다가 입력값중 가장 홀수를 뺌 => 답
'''
import time
start = time.time()

n = int(input())
a = [*map(int, input().split())]
s,l = [sum(a), len(a)]

if print(0) if l ==1 and a[0] % 2 == 1 else print(a[0]) if l == 1 else True:
    if print(s) if s % 2 == 0 else True:
        o = [ a[i] for i in range(0,n) if a[i] % 2 == 1]
        print(s- min(o))


#print(0) if len(a)==1 and a[0] % 2 == 1 else print(0) if len(a) != 1 else y = False
print(c=False)


end = time.time()
print(start - end)