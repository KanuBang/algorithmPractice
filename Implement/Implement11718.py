import sys
input = sys.stdin.readline
ans = []


for i in range(0,100):
    str = input()
    if str == '\n':
        break
    ans.append(str)
for i in ans:
    print(i.rstrip())