import sys
input = sys.stdin.readline

x = []
xSet = []
y = []
ySet = []

for i in range(0,3):
    msg = input().rstrip().split()
    x.append(int(msg[0]))
    y.append(int(msg[1]))

xSet = list(x)
ySet = list(y)


for i in range(0,len(xSet)):
    if x.count(xSet[i]) == 1:
        print(xSet[i], end = " ")
        break
for i in range(0,len(ySet)):
    if y.count(ySet[i]) == 1:
        print(ySet[i])
        break
