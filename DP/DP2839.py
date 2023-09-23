'''

입력:
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
'''

d = [-1] * 5001
d[3] = 1
d[5] = 1

n = int(input())

for i in range(6, n+1):

    f = 1000
    s = 1000
    if d[i-3] != -1:
        f = d[i-3] +d[3]
    
    if d[i-5] != -1:
        s = d[i-5] + d[5]

    if d[i-3] == -1 and d[i-5] == -1: 
        f = -1

    d[i] = min(f,s)
        
print(d[n])