n = int(input())
d = [0] * 1001

arr = [int(input()) for i in range(n)]

if len(arr) <= 2:
    print(sum(arr))
    exit()

d[0] = arr[0]
d[1] = d[0] + arr[1]

for i in range(2,n):
    d[i] = max(d[i-2]+ arr[i], d[i-3]+arr[i-1]+arr[i])

print(d[n-1])
