'''
1 초	256 MB
N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

=> 왠만하면 O(n)?

1. n과 k를 입력받는다.
2. 동전을 입력받는다.
3. 동전의 액면가가 큰 순으로 내림차순 정렬 한다.
4. 만약 현재의 동전 액면가가 합보다 작거나 같다면
   현재 추가되는 동전의 개수는 = 현재 합 // 현재 동전의 액면가
   현재 합 = 현재 합 - 현재 추가되는 동저의 개수 * 현재 동전의 액면가
   총 추가되는 동전의 개수 = 총 추가되는 동전의수 + 현재 추가되는 동전의 개수이다.
   반면, 반대 상황이라면 그 동전은 추가될 수 없고 다음으로 큰 동전으로 현재 작업을 수행한다.
5. 4를 반복하다 보면 최솟값이 구해진다.
'''

import sys
input = sys.stdin.readline

n,k = map(int, input().rstrip().split())
coins = []
idx,cnt = (0,0)

for i in range(n):
    coins.append(int(input().rstrip()))

coins.sort(reverse=True)

while k > 0:
    
    if coins[idx] > k:
        idx += 1
    else:
        add = k // coins[idx]
        k -= add * coins[idx]
        cnt += add

print(cnt)
