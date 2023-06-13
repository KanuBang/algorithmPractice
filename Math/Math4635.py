import sys
input = sys.stdin.readline

n = 0 
ans = []
total = 0
dif = 0
while n != -1:
    n = int(input().rstrip())
    for i in range(0,n):
        msg = list(map(int, input().rstrip().split()))
        if i == 0:
            total += msg[0] * msg[1]
            dif = msg[1]
        else:
            total += msg[0] * (msg[1]-dif)
            dif = msg[1]
    
    ans.append(str(total) + " miles")
    total = 0

for i in range(0, len(ans)-1):
    print(ans[i])
