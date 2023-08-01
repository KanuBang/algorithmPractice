'''

2초
128MB
N은 100보다 크거나 같고, 2,000,000,000
근데 어차피 뒤에 저 두자리만 보는 거니까 10 * 10 = 100 이라서 부담 없을 듯 하다. 이론상 n^3도 가능함

'''

'''
문제해결
1. 숫자를 받음
2. 뒤의 두자리를 00으로 받음
3. +1 씩 반복해서 올림
4. 나누어 떨어지는 수간 최소임. 이때 break
5. 탈툴
'''

n = int(input())
m = int(input())

a = list(str(n))
a[len(a)-1] = '0'
a[len(a)-2] = '0'
n = int("".join(a))
cnt = 99
i = 0
ans = 0
while i <= cnt:
    if n % m == 0:
        ans = str(i)
        break
    i += 1
    n += 1

if len(ans ) == 1:
    print("0",end="")
    print(ans)
else:
    print(ans)

