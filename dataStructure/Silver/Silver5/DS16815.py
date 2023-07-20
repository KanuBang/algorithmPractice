'''
2 초	512 MB 
The length of $S$ is between $1$ and $100$, inclusive.
사이즈가 적어서 별 문제 없을 거 같음
물론, 2중, 3중 ... 되면 문제 발생 가능 

((*)())

) ) ( ) * ( ( 
( ( * ) ( ) )

()*()
( ) * ( )

1. * 이전까지는 ( 을 카운트하고 이후에는 )을 카운트한다
2. 단, )이 나오고 이전게 ( 라면 카운트를 감소한다
()*()
((((((((((*)))))))))) 10 10 => 10
((*)()) 2 2 => 2
(()())* 1 0 => 0
((*)() 2 1 -> 1
(*)() 1 1-> 1
)()*()(
'''

import sys
input = sys.stdin.readline

arr = [ i for i in input().strip()]
tar = "("
prohibit = ")"
before = None
left = 0
rihgt = 0
for i in arr:
    if i == "*":
        tar = ")"
        prohibit = "("
        before = "*"
        continue
    
    if i == tar:
        if tar == "(":
            left += 1
        else:
            rihgt += 1
    else:
        if before == tar:
            if tar == "(":
                left -= 1
            else:
                rihgt -= 1
        
    before = i

print(min(left,rihgt))