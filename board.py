r,c = map(int, input().split())
cnt = 2
one = []
two = []
ans = 0
while cnt > 0:
    if cnt == 2:
        for i in range(c):
            tar = list(map(int, input().split()))
            one.append(tar)
    else:
        for i in range(c):
            tar = list(map(int, input().split()))
            two.append(tar)
    cnt -= 1

for i in range(c):
    for j in range(r):
        print(one[i][j] + two[i][j], end=" ")
    print()