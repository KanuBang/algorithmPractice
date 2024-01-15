import sys
input = sys.stdin.readline

n,m = map(int, input().split())
hashMap = {}

for i in range(1,n+1):
    monster = input().rstrip()
    hashMap[str(i)] = monster
    hashMap[monster] = str(i)

for i in range(m):
    print(hashMap[input().rstrip()])