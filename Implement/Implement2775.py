import time
t = int(input())

for i in range(t):
    k = int(input())        # 층
    n = int(input())        # 호
    start = time.time()
    people = [i for i in range(1, n+1)]     # 0층

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y+1]))   # 아래층의 1~n호 까지의 합
        people = new.copy()
        #print(people)		# peaple에 들어있는 값 출력해 봄
    print(people[-1])       # K층 n호
    end = time.time()
    #print(end-start)

    '''
    2층 3호

    "1층"
    people = [ 1 2 3 ]
    
    y=0
    [:1] = 1 append

    y=1
    [:2] = 3 append

    y=2
    [:3] = 6 append

    => new [1,3,6]
    => copy to people
    people [1,3,6]

    "2층"
    y=0
    [:1] = 1 append

    y=1
    [:2] = 4 append

    y=2
    [:3] = 10 append
    => ㅜㄷㅈ [1,4,10]
    => copy to people
    => people[1,4,10]


    print(people[-1]) = 10

    
    '''


