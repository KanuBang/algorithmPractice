n,g = list(map(int,input().split()))

mat =[]
for i in range(g):
    num = int(input())
    while num > 0:
        mat.append(num) if num == 1 else mat.append(2)
        num -= 2

if len(mat) > n:
    sum = sum(mat[n:])
    i = 0
    while sum != 0:
        if mat[i] == 1:
            mat[i] +=1 
            sum -= 1
        i += 1
        
for i in range(n):  
    print(0) if i > len(mat) - 1 else print(mat[i]) 