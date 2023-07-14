""" 
I LOVE YOU
I LOVE MUSTARD
HAPPY BIRTHDAY
GLAD U BORN
SMILE
IMAGINE
WHATS UP DOC
HAVE A NICE DAY
END
"""
from collections import deque

bundle = [None]
while bundle[-1] != "END":
    bundle.append(input())

for i in bundle:
    pr = True
    if i == None:
        continue
    elif i == "END":
        break
    else:
        k = list(i)
        while len(k) > 1:
            target = k.pop()
            if target == ' ':
                continue
            for j in k:
                if j == target:
                    pr = False
                    break
    if pr == True:
        print(i)
    



