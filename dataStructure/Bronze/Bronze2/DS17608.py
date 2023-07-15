
""" 
시간 제한	
1 초 (추가 시간 없음)
- N의 범위가 100000(십만)인 경우 ⇒ O(nlogn)
- N의 범위가 10000000(천만)인 경우 ⇒ O(n)
메모리 제한
512 MB

입력
첫 번째 줄에는 막대기의 개수를 나타내는 정수 N (2 ≤ N ≤ 100,000)이 주어지고 
이어지는 N줄 각각에는 막대기의 높이를 나타내는 정수 h(1 ≤ h ≤ 100,000)가 주어진다.

출력
오른쪽에서 N개의 막대기를 보았을 때, 보이는 막대기의 개수를 출력한다. 
'''
5 3 7 1 => 2개

6, 9, 7, 6, 4, 6 => 3개

1. 5 3 7 1
2. 1
3. 5 > 1, 3 > 1, 7 > 1
4. 5 3 7
5. 5 < 7, 3 < 7

그러니까 top 수보다 큰 수가 없으면 탈출

6 9 7 6 4 6
6 9 7 6 4
=> top 보다 모두 다 큼 
6 9 7 6
=> top 보다 모두 다 크 거나 같음
6 9 7



6 9 7 6 4 6

가장 큰 것 보다 뒤는 볼 필요가 없음
9 7 6 4 6
이 상태에서 top보다 큰 거만 체킹하면 됨


5 3 7 1

5 4 3 2 1
'''

해결:
0. 읽는다
1. 가장 큰 숫자에 접근한다
-max로 찾고 인덱스로 접근한다
2. 팝한 숫자와 비교
3. 크면 카운트
시간복잡도 n예상
"""

import sys
import time

input = sys.stdin.readline
n = int(input())

start = time.time()
nums = []
cnt = 1
tar = []
top = 0
max = 0
max_idx = 0
for i in range(n):
    nums.append(int(input()))
    if max <= nums[i]:
        max = nums[i]
        max_idx = i

top = nums.pop()
tar = nums[max_idx:]
before = 0

for i in tar:
    if i > top and i != before:
        cnt += 1
    before = i
print(cnt)
end = time.time()
print(end-start)


