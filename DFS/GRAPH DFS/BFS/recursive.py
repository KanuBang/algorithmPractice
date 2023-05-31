def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출한다')
    recursive_function(i+1)
    print(i,  '번째에서 재귀 함수를 종료한다')

#recursive_function(1)

def factorial_recursive(i):
    if i == 0:
        return 1
    
    return i*factorial_recursive(i-1)

print('재귀적: ', factorial_recursive(4))


'''
5
4
3
2
1
0


0->return 1
1-> return 1*1
2-> 2*1*1
3-> 3*2*1*1
4-> 4*3*2*1*1
4 -> 5*4*3*2*1*1



5 * 4 * 3 * 2 

'''
