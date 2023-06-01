'''


'''



import sys

input = sys.stdin.readline

n = int(input())
star = 1

for i in range(0,n*2-1):
    
    if i < n-1:
        print("*"*star, end = " ")
        star += 1
    else:
        print("*"*star, end=" ")
        star -= 1

    print()