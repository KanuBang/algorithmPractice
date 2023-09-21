d = [0] * 100
d[1] = 1
d[2] = 2
d[3] = 4

n = int(input())
ans = []
for i in range(0,n):
    k = int(input())
    for x in range(4,k+1):
        d[x] = d[x-1] + d[x-2] + d[x-3]
        
    ans.append(d[k])


for i in ans:
    print(i)