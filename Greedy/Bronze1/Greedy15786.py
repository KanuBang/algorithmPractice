
""" 
4 5
PPAP
PPAPP
PPPPA
APPPP
PPPAP
PAPAP 
"""

'''
시간: 
N의 범위가 500인 경우 ⇒ O(n3)
N의 범위가 2000인 경우 ⇒ O(n2)

입력의 첫째 줄에 석규가 기억하는 원본 알파벳의 수 N(1 ≤ N ≤ 100)과 포스트잇의 개수 M(1 ≤ M ≤ 1000)이 주어진다. 
다음 줄에 길이가 N인 알파벳 대문자로 이루어진 문자열 S가 주어진다. 
이 후 M개의 줄에 알파벳 대문자로 이루어진 판별해야 할 포스트잇들이 주어진다. 모든 포스트잇에 적힌 문자열은 1000자 이하이다.


이 두 가지 사항을 고려해봤을 때 n^3도 가능하지 않을까? 생각해봤음

공간:
4MB 백만 int 리스트 기준 512MB는 넉넉해 보임

'''
n,m = [* map(int, input().split())]
target = input().rstrip()
post = [input().rstrip() for i in range(m)]

for i in range(0,m):
    b,cnt = (0,0)
    memo = list(post[i])
    for j in list(target):
        for k in range(b,len(memo)):
            b += 1
            if j == memo[k]:
                cnt += 1
                break
    print("true") if cnt == n else print("false")
 
            
        
        
