import sys
input = sys.stdin.readline
ans = []
num = 0

for i in range(0,5):
    num = int(input())
    if num < 40:
        num = 40
    ans.append(int(num))

print(int(sum(ans)/ 5))
