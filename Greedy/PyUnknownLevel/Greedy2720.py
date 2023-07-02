import sys
input = sys.stdin.readline

n = int(input().rstrip())
tools = [25,10,5,1]
ans = []
cnt = 0

for j in range(0,n):
    num = int(input().rstrip())
    for i in range(0,4):
        ans.append(num // tools[i])
        num = num % tools[i]


for i in range(0,len(ans)):
    print(ans[i], end = " ")
    cnt += 1
    if cnt % 4 == 0:
        print()