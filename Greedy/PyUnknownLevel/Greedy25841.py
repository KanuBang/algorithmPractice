import sys
input = sys.stdin.readline

msg = list(map(int,input().split()))
ans = 0

for i in range(msg[0],msg[1]+1):
    ans += str(i).count(str(msg[2]))

print(ans)