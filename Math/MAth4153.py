'''
1. 입력받고
2. 리스트를 만들고
3. 최대를 찾고 최대를 리스트에서 빼낸다.
4. 최대가 0이면 break.
5. pop 한 값 제곱의 합과 같으면 right 출력 아니면 wrong 출력
'''


import sys
input = sys.stdin.readline

myList = []

while True:
    msg = input().rstrip()
    myList = list(map(int, msg.split(' ')))
    max_sqaure = pow(max(myList),2)
    max_val = pow(max_sqaure, 0.5)
    if  max_sqaure == 0:
        break
    else:
        for i in myList:
            if max_val == i:
                continue
            max_sqaure -= pow(i,2)
    
    print("right") if max_sqaure == 0 else print("wrong")
    myList = []