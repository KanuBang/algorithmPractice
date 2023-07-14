'''
입력:
    10
    hippo_in_tank 1

    lazy_hippo 2

    hippo_vampire 
    bizarre_hippo
    hippo_in_tank 1
    hippo_ninja
    hippie_hippo 
    lazy_hippo 2
    hippo_in_tank 1
    hip_hop_hippo 

출력:
    3


The first line contains integer 
$n$ (
$2 \le n \le 100$).

범위가 500이하 라서 시간제한은 n^3여도 크게 제한을 안 받을 거 같고
메모리도 정수 리스트 100만 기준 4MB면 딱히 위험성이 없어 보인다
시간제한:1초
메모리제한:64MB


풀이:
1.개수를 입력받는다
2.문자열을 리스트에 저장
3.가장 맨끝에 있는 것을 pop
4.같은게 있는지 체크
5. 끝까지 했는데도 같은게 없다면 정답+1, 
6.같은게 하나라도 발견되면 del



hippo_in_tank hippo_in_tank hippo_in_tank
lazy_hippo lazy_hippo

hippo_vampire
bizarre_hippo
hippo_ninja
hippie_hippo
hip_hop_hippo

'''

store = [input().rstrip() for i in range(int(input()))]
print(len(store) - len(list(set(store))))

'''
while len(store) >= 1:
    ans = True
    tar = store.pop()
    for i in store:
       
        if store[store.index(i)] == tar:
           del store[store.index(i)]
           ans = False

    if ans == True and len(store) != 0:
        k.append(tar)
    elif len(store) != 0:
        print(store)
        same += 1
'''

#print( n - (len(k) + same))
