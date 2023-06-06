import sys

input = sys.stdin.readline
n = int(input().rstrip())
ans = []
str = ""
while n > 0:
    msg = input().rstrip()
    tmp = ""
    for i in range(0,len(msg)):
        if msg[i] == tmp:
            continue
        else:
            str += msg[i]
        
        tmp = msg[i]

    ans.append(str)
    str = ""
    n -= 1

for i in ans:
    print(i)