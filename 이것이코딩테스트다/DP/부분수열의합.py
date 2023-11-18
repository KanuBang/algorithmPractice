c = [0,75,105,120,75,90,135]
dp = [0] * 1000
dp[1] = 75
dp[2] = 105

for i in range(3,len(c)):
    dp[i] = max(dp[i-1], dp[i-2]+c[i])

print(i)
print(dp[i])