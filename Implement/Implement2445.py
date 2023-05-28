'''
*        *  8 2 / 0 9 / 1 8
**      **  6 4 / 1 8 / 2 7 
***    ***  4 6 / 2 7 / 3 6
****  ****  2 8 / 3 6 / 4 5
**********  0 10 / 4 5 
****  ****  2 8  / 3 6 / 4 5
***    ***  4 6 / 2 7  / 3 6
**      **  6 4 / 1 8  / 2 7
*        *  2 8 / 0 9  / 1 8
'''

import sys
input = sys.stdin.readline

n = int(input())
star = 1
empty = n*2-2

for i in range(0, n*2):
    print("*"*star + " " * empty + "*"*star + " ")
    if i < n - 1:
        star += 1
        empty -= 2
    else:
        star -= 1
        empty += 2