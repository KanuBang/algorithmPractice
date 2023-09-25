d = [1,2]
n = int(input())
if n == 1:
    1
else:
    for i in range(2, n):
        d.append((d[i-1]+d[i-2]) % 10007)
print(d[n-1])