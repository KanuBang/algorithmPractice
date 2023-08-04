'''
16 4
noj.am IU
acmicpc.net UAENA
startlink.io THEKINGOD
google.com ZEZE
nate.com VOICEMAIL
naver.com REDQUEEN
daum.net MODERNTIMES
utube.com BLACKOUT
zum.com LASTFANTASY
dreamwiz.com RAINDROP
hanyang.ac.kr SOMEDAY
dhlottery.co.kr BOO
duksoo.hs.kr HAVANA
hanyang-u.ms.kr OBLIVIATE
yd.es.kr LOVEATTACK
mcc.hanyang.ac.kr ADREAMER
startlink.io
acmicpc.net
noj.am
mcc.hanyang.ac.kr

첫째 줄에 저장된 사이트 주소의 수 N(1 ≤ N ≤ 100,000)과 비밀번호를 찾으려는 사이트 주소의 수 M(1 ≤ M ≤ 100,000)이 주어진다.

=> 이중 루프면 딱봐도 터짐 n으로 짜라는 말

1. 일단, 사이트:비밀번호 형태로 dict에 저장하고
2. 그리고 key로 찾자
'''

import sys
input = sys.stdin.readline

sites, n = map(int,input().split())
myDict = dict()
for i in range(sites):
    site = input().strip().split()
    myDict[site[0]] = site[1]

for i in range(n):
    print(myDict[input().strip()])