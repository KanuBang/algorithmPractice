import sys

input = sys.stdin.readline

n1,k1,n2,k2 = map(int,input().split())
val = n1*int(k1) + n2*int(k2)
print(val)