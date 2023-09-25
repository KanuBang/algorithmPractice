import sys
input = sys.stdin.readline

n = int(input())
nums = []
start,end = (0,-1)
for i in range(n):
    nums.append(list(map(int,input().split())))

for i in range(1,n):
    size = len(nums[i])
    end += 1
    for j in range(size):
        if j == start:
            nums[i][j] += nums[i-1][start]
        elif j == size - 1:
            nums[i][j] += nums[i-1][end]
        else:
            nums[i][j] += max(nums[i-1][j],nums[i-1][j-1])
    


print(max(nums[i]))
        

