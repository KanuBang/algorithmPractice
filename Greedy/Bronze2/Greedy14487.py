'''
2초 512MB
int 기준 백만 배열이 4MB
따라서 512 / 4 = 128

1000000 * 128 
= 128000000 = 12억 8천만 크기인 int 리스트 가능
1<=n<=50000

시간과 공간은 딱히 제약이 있어 보이지 않음.
'''

'''

1. 그리디: 현재 상황에 가장 최선의 아이디어
=> 리스트에서 가장 큰 수를 빼고 합을 구한다
1) 입력
2) 리스트 에서 가장 큰 수를 찾음
3) 그 max를 제외한 합을 구함

2. 검증
max가 중복되는 경우
=> max를 위한 카운트 값을 만들고
=> 그 값이 0이 아니면 중복되더라도 합함
'''

import time
start = time.time()

input()
a=[*map(int,input().split())]
print(sum(a)-max(a))

end = time.time()
print(end - start)