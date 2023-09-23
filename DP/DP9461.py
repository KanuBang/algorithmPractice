d = [0] * 1001
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
for i in range(int(input())):
    t = int(input())
    if 1 <= t and t <= 4:
        print(d[t])
        continue
    for i in range(5,t+1):
        d[i] = d[i-5] + d[i-1]
    print(d[t])