line = int(input().rstrip())
maxWeight = [int(input().rstrip()) for i in range(0,line)]
maxWeight.sort()

ans = []
k = line

for i in range(0,line):
    ans.append(maxWeight[i]*k)
    k -= 1

ans.sort()
print(ans[-1])





