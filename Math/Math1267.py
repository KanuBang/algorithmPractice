import sys
input =sys.stdin.readline

n = int(input().rstrip())
line = input()
(y, m) = (0,0)

for i in list(map(lambda x: int(x),line.split(' '))):
    y += ((i // 30) + 1) * 10
    m += ((i // 60) + 1) * 15

print('Y M %d' %y) if y == m else print("Y %d" %y) if y < m else print("M %d" %m)

