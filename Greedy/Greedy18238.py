'''
시간복잡도:
제한 -> 1초
범위 -> 문자열의 최대 길이는 100자


o(n^3)도 잘하면 가능할 듯
시간복잡도는 여유 넘침


공간복잡도:
제한 -> 512MB
int리스트 백만 -> 4MB
512MB -> int리스트 12억 8천만

문자열의 길이는 최대 100자 -> 


설계:
- 빈 문자열과 출력에 걸리는 시간은 없다
- 한 칸 이동해 1초
- 왼쪽 오른쪽 가능


ZOAC
Z -> 1초 (왼쪽)
O -> 11초 (왼쪽)
A -> 12초 (왼쪽)
C -> 2초 (오른쪽)


ZOAC = 26
현재 가리키고 있는 것에 13번째 부터는 -> 오른쪽
14번째는 -> 왼쪽이나 오른쪽이나 노상관
14번째 이후는 -> 왼쪽이 유리

ptr: A = 1
find: Z = 26

1 + 25 = 26
26 - 1 = 25

1 + 
'''

'''
ZOAC = 26
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25

만약 차이가 13이면 왼쪽이든 오른쪽이든 13이고
12이하면 왼쪽이고
14이상이면 오른쪽이다

A = 0
Z = 25
|0-25| = 25
1,25

Z = 25
O = 14
|25-14| = 11 -> 왼쪽
26 - 11 = 15
11,15

O = 14
A = 0
|14-0| = 14
26-14 = 12

12,14

'''

import time
from string import ascii_uppercase

start_time = time.time()

s = input()
alphabet_list = list(ascii_uppercase)
ptr = 'A'
sum = 0

for i in s:
    val = abs(alphabet_list.index(ptr) - alphabet_list.index(i))
    sum += min(val, 26-val)
    ptr = i

print(sum)



end_time = time.time()

print(end_time-start_time)