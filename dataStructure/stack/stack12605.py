'''
import sys
input = sys.stdin.readline

n = int(input())
newStr = []
str = ""
ans= []

for i in range(0, n):
    str = input().strip()
    listStr = str.split(' ')

    for i in range(len(listStr)-1,-1,-1):
        newStr.append(listStr[i])
    
    str = " ".join(newStr)
    ans.append(str)

    str = ""
    newStr = []


for i in range(0,n):
    print("Case #{0}: ".format(i+1), end="")
    print(ans[i])
'''


import sys

for i in range(int(sys.stdin.readline())):
    print(f'Case #{i+1}:', ' '.join(sys.stdin.readline().split()[::-1]))
