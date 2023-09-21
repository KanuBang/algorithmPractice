'''

입력:
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
'''

d = [-1] * 5001
d[3] = 1
d[5] = 1

n = int(input())


for i in range(6, n+1):

    first = 100000
    second = 100000
    if d[i-3] != -1:
        # d[i] = d[i-3] + d[3]
        first = d[i-3] +d[3]
    
    if d[i-5] != -1:
        # d[i] = d[i-5] + d[5]
        second = d[i-5] + d[5]

    if d[i-3] == -1 and d[i-5] == -1: 
        first = -1

    d[i] = min(first,second)
        

print(d[n])