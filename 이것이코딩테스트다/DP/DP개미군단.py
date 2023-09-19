n = int(input())
array = list(map(int, input().split()))

d = [0] * 100 # 각 지점을 털때 뭐가 최선인 지를 알려주는 DP 테이블

d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,n):
    print(d[i-1])
    print(d[i-2])
    d[i] = max(d[i-1],d[i-2]+array[i])

print(max(d))