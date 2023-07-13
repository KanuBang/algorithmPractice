'''
2 초	
A line contains no more than 80 characters.
=> N이 500인경우가 n^3 허용인데 80이면.. 게다가 2초면...시간은 상관 안 써도 될 듯

512 MB
=> 공간도 넉넉해보임(참고 정수 리스트 기준 백만 일시 4MB)

문제
There is a game in which you try not to repeat a word 
while your opponent tries to see if you have repeated one.
"THE RAIN IN SPAIN" has no repeats.
"IN THE RAIN AND THE SNOW" repeats THE.
"THE RAIN IN SPAIN IN THE PLAIN" repeats THE and IN.
Write a program to test a phrase.

입력
Input is a line containing words separated by single spaces, 
where a word consists of one or more uppercase letters. 
A line contains no more than 80 characters.

출력
The output is "yes" if no word is repeated, and "no" if one or more words repeat.

THE RAIN IN SPAIN
yes

IN THE RAIN AND THE SNOW
no

THE RAIN IN SPAIN IN THE PLAIN
no


풀이
1. 문장을 공백 기준으로 나눠서 리스트에 저장
2. 그 단어가 있는지 체크
3. ans는 default로 YES 해놓고 그 단어가 있으면 no로 바꿈
4. 하나라도 있는 순간 no 출력하고 프로그램 종료
'''
words = input().split()
ans = "yes"
number = 1



while len(words) > 1:
    target = words.pop()
    for i in words:
        if i == target:
            ans = "no"
            break


print(ans)

'''
i show speed

'''
