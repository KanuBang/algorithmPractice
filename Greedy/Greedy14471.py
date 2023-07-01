import time
'''
시간: 2 초	
음.. 왠마하면 문제 없을 듯

공간: 512 MB
음.. 이것도 왠만하면 문제 없을 듯
int 기준
백만 => 4MB
12억 8천만 => 512MB


풀이:
4 5

4 * 2 중 4개 이상 이어야 경품 교환 가능 => 경품 교환권
경품 교환권 5개가 목표

1 7 => 여기 3개
6 2 => ㅇㅋ
3 5 => 여기 1개
4 4 => ㅇㅋ
0 8


그래서 총 4개


'''

start = time.time()

n,m = list(map(int, input().rstrip()))
ans = 0
for i in range(m):
    o,x = list(map(int, input().rstrip()))
    if o >= n:
        ans += 1

if ans < m


end = time.time()
print(start - end)