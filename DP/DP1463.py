d = [0] * 10000001

x = int(input())

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[x])


# 첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.