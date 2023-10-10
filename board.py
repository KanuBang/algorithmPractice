import math
import random

ans = []
n = int(input())
for i in range(1,n):
    for j in range(1,n):
        ans.append(i*j)

for i in range(n):
    print(ans[i], end=' ')


print(random.randrange(1,49))