n = int(input())
d = [0] * (n+1)
k = list(map(int, input().split()))

for i in range(1,n+1):
    if i == 1:
        d[i] = 1
    elif k[i-1] > k[i-2]:
        d[i] = d[i-1] + 1
    else:
        d[i] = d[i-1]

print(d)
print(d[n])

