import sys
input = sys.stdin.readline

time = list(map(int, input().rstrip().split()))
runtime = [0,0,0]
ans = []
carry = 0
num = int(input().rstrip())

runtime[2] = num % 60
runtime[1] = num 

for i in range(2,-1,-1):
    if i == 0:
        runtime[i] = num
        break
    runtime[i] = num % 60
    num = num // 60

for i in range(2,-1,-1):
    sum = runtime[i] + time[i] + carry
    if i != 0 and sum >= 60:
        ans.append(sum % 60)
        carry = sum // 60

    elif i == 0 and sum >= 24:
        ans.append(sum % 24)
    else:
        ans.append(sum)
ans.reverse()

print(ans[0],ans[1],ans[2])

