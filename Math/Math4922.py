import sys
input = sys.stdin.readline

ans = [ ]
num = int(input().rstrip())

while num != 0:
    ans.append((num,num*(num-1)+1))
    num = int(input().rstrip())

for i in range(0,len(ans)):
    msg = str(ans[i][0]) + " => " + str(ans[i][1])
    print(msg)