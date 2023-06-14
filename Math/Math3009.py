import sys
input = sys.stdin.readline

x = []
y = []
ans = []
for i in range(0,3):
    msg = input().rstrip().split()
    x.append(int(msg[0]))
    y.append(int(msg[1]))

ans.append(x)
ans.append(y)

for k in range(0,2):
    for i in range(0,len(ans[k])):
        if ans[k].count(ans[k][i]) == 1:
            print(ans[k][i], end = " ")
            break

