import sys
input = sys.stdin.readline

n = int(input())
left = n - 1
right = n - 1

for i in range(0,n):
    for j in range(n*2-1):
        if j < left:
             print(" ", end="")
        elif left <= j and j <= right:
            print("*", end="")
        elif j == right+1:
            print(" ", end="")
            break
        
        
    
    left -= 1
    right += 1
    print()