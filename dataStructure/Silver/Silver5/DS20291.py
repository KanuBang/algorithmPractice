'''
50000이라서 2중 루프만 되도 위험함. 근데 3초라서 가능할지도?
이럴때는 리스트보다 더 빠른 딕셔너리를 사용
8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt
'''

import sys
input = sys.stdin.readline

myFiles = dict()

for i in range(int(input())):
    extensions = (input().strip().split('.'))[1]

    if extensions not in myFiles.keys():
        myFiles[extensions] = 1
    
    else:
        myFiles[extensions] += 1

sort_dict = sorted(myFiles.items(), key=lambda x: x[0], reverse=False)
for i in sort_dict:
    print(i[0], i[1], end = " ")
    print()
'''
import sys
input = sys.stdin.readline

n = int(input())

file = dict()
for _ in range(n):
    extend = (input().split('.'))[1]
    if not extend in file:
        file[extend] = 1
    else:
        file[extend] += 1

sort_file = sorted(file.items())

for key, value in sort_file:
    print(key.rstrip(), value)

'''

