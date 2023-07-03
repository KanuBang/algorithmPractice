'''
시간:1초

제한:1024MB
리스트 정수 백만 4MB

별 문제 없을 듯

'''

a,b,c,m = [* map(int, input().split())]

stamina = 0
work = 0
time = 0
i = 1


if a > m:
    print(0)
    exit()

while time < 24:
    while a <= m:
        stamina += a
        work += b
        time += 1
        if time == 24:
            print(work)
            exit()
        if stamina + a > m:
            break

    while True:
        stamina -= c
        time += 1
        if stamina < 0:
            stamina = 0
        if stamina + a <= m:
            break

print(work)

    