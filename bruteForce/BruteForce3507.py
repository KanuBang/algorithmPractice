import sys
input = sys.stdin.readline
n = int(input().rstrip())
cnt = 0
if n>=199:
    print(0)
    exit()
down = n // 2
up = n - down

while up < 100:
    if down == up:
        cnt += 1
    else:
        cnt += 2
    
    down -= 1
    up += 1

print(cnt)
