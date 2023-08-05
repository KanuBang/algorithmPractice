'''
4
4 MISSPELL
1 PROGRAMMING
7 CONTEST
3 BALLOON

MISPELL
ROGRAMMING
CONTES
BALOON

 T(1<=T<=1,000)
 1 초	128 MB
 n으로 푸는게 정배일 듯
'''

ans = []
for i in range(int(input())):
    idx,str = input().split()
    strList = list(str)
    del strList[int(idx)-1]
    str = "".join(strList)
    print(str)