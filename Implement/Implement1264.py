'''
How are you today?
Quite well, thank you, how about yourself?
I live at number twenty four.
#

7
14
9
'''

consonats = ['a','e','i','o','u']
bigConsonants = ['A', 'E', 'I', 'O', 'U']
ans = []
while True:
    cnt = 0
    str = input()
    if str == '#':
        break
    else:
        for i in str:
            if i in consonats or i in bigConsonants:
                cnt += 1
    
    ans.append(cnt)


for i in ans:
    print(i)