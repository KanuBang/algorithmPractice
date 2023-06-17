import sys
input = sys.stdin.readline

n = int(input())
ans = []
sum = 0
min = 0
cnt = 0
for i in range(0,n):
    ans.append(list(map(int, input().rstrip().split())))

for i in range(0,n):
    ans[i].sort()
    for j in range(0,7):
        if ans[i][j] % 2 == 0:
            cnt += 1
            sum += ans[i][j]
            if cnt == 1:
                min = ans[i][j]
    
    print(sum, end =" ")
    print(min)
    sum = 0
    min = 0
    cnt = 0
