
d = [0] * 1001
d[0] = [1,0]
d[1] = [0,1]

for i in range(int(input())):
    t = int(input())

    for i in range(2, t+1):
        d[i] = [d[i-1][0]+d[i-2][0],d[i-1][1] +d[i-2][1]]        

    print(' '.join(map(str,d[t]))) 