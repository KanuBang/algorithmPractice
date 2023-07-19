'''
The first line of input contains a single integer P, (1 ≤ P ≤ 1000), 
which is the number of data sets that follow.
Each data set consists of a line containing the number n of the c (1 ≤ n ≤ 100), 
a space and the number m of results to centralize (1 ≤ m ≤ 1000) and followed by n lines and m lines.
The n lines contain the names of c, one per line. The m lines contain each a name X of one candidate, a space, the result R of the candidate and the center C of vote. X and C are strings that will contain at most 1000 characters. R is a positive integer.

1 ≤ P ≤ 1000
1 ≤ n ≤ 100
1 ≤ m ≤ 1000
그냥 n 일시 n^2도 될 거 같다.
하지만 이중 루프 일시에는 로그선형 이하여야 한다

2
3 4
Bignon
Akwaba
Sessi
Bignon 1000 Gbegamey
Sessi 1000 Yenawa
Akwaba 5 Vodje
Akwaba 996 Yenawa
2 3
Sena
Sedjro
Sedjro 6003 Malanville
Sena 6000 Kpankpan
Sena 3 Godomey

VOTE 1: THE WINNER IS Akwaba 1001
VOTE 2: THERE IS A DILEMMA
'''

import sys
input = sys.stdin.readline

for i in range(int(input())):
    c = {}
    n,m = [* map(int, input().split())]
    for j in range(n):
        c[input().strip()] = 0
    for k in range(m):
        s = input().split()
        c[s[0]] += int(s[1])
    
    a = list(c.values())
    
    if a.count(max(a)) > 1:
        print('VOTE %d: THERE IS A DILEMMA' %(i+1))
        continue
    for e in c:
        if c[e] == max(a):
            print("VOTE %d: THE WINNER IS %s %d" %(i+1,e,max(a)))
            break

    
