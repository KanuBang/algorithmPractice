'''

시간: 1초
범위: 테스트 케이스에 대한 정보는 없음

공간: 1024MB
백만 정수 리스트 4MB
=> 이거는 뭐 거의 무제한

2
99 => 111
1234 => 1235


설계

99
100 101 102

1. 문자를 숫자로 변환
2. 0이 있는 지 체크
3. 0이 없으면 다음 수, 0이 있으면 continue
'''

import time
start = time.time()
n = int(input().rstrip())
ans = []
for i in range(n):
    k = int(input().rstrip()) + 1
    while '0' in str(k):
        k = k + 1
    ans.append(k)

for i in range(n):
    print(ans[i])


end = time.time()
print(end - start)