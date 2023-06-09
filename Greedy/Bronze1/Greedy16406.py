'''
시간: 2초
범위: Bounds are 0 ≤ k ≤ n ≤ 1000; 1 ≤ n.
n^3는 불가능

공간: 512MB
128 * 백만 => 1억 2천 8백만
'''

'''
문제해결: 
6
TTFTFFTFTF
TTTTFFTTTT
9


내 친구가 정답일때 나도 정답이고
내 친구가 틀렸을때 내가 정답이면 => 내가 최대 점수임

즉, 

그니까 같은 답은 골랐을 때가 정답이야 최대 점수를 얻을 수 있다.
T T F T F F T F T F
T T T T F F T T T T

같은 답: 7
다른 답: 3
친구의 맞은 답: 6
같은답 + (다른 답 - (친구 답 - 같은 답))

7 + (3 - |(6 - 7)|)


3
F T F F F 
T F T T T 

같은 답: 0
다른 답: 5
친구의 맞은 답: 3
내 최대: 2
같은답 + (다른 답 - (친구 답 - 같은 답))
0 + (5 - (3))

F F T
T T F

같은 답:2
다른 답:2
친구의 답: 1
내 최대: 1

답이 같았을 때 같이 맞아야 좋은 거임
그리고 개가 틀렸을 대 내가 맞아야 좋은 거고

1) 만약 서로 찍은 답이 완전히 다르면
=> 친구가 틀린만큼 내가 맞은 거임(전체-친구의 맞은 답 개수)

2) 만약 서로 찍은 답이 완전히 같으면
틀릴 때도 맞을 때도 같은 점수를 얻기에
=> 친구의 점수가 곧 내 점스(친구의 답 개수)

3) 적절하게 섞여 있을 경우
다른 답 + 친구가 맞은 답

3
TTTT
TFFF
6

같은 답: 1
다른 답: 3
친구 답: 3

1
같은답 + (다른 답 - (친구 답 - 같은 답))

1 + (3 - (3 - 1))


아 이게 공식이네

같은답 + (다른 답 - (친구 답 - 같은 답))
'''


import time
start = time.time()


'''
for i in range(len(f)):
   if f[i] == m[i]:
       s += 1
   else:
       d += 1
'''
n = int(input())
f = input()
m = input()
a=0
k = [ 1 if f[i] == m[i] else 0 for i in range(len(f))]
s,d = (k.count(1), k.count(0))
print(s + (d - abs(n-s)))

#같은답 + (다른 답 - (친구 답 - 같은 답))
end = time.time()
print(end-start)