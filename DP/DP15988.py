d = [0,1,2,4]

for i in range(4, 1000001):
    d.append((d[i-1] + d[i-2] + d[i-3]) % 1000000009)

for j in range(int(input())):
    print(d[int(input())])
