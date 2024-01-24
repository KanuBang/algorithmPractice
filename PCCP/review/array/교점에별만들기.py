def solution(line):
    answer = []
    intersect = []
    
    for i in range(len(line)):
        a,b,e = line[i]
        for j in range(i+1, len(line)):
            c,d,f = line[j]
            denom = a*d - b*c
            if denom == 0:
                continue
            # 교점 구하기
            x = (b*f - e*d) / denom
            y = (e*c - a*f) / denom
            
            # 정수 교점만 남기기 -> 여기가 진짜 포인트다.
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                intersect.append([x,y])
            
    # ax = ay = [] 같은 메모리 참조
    ax,ay = [],[]
    for star_x, star_y in intersect:
        ax.append(star_x)
        ay.append(star_y)
    min_x, min_y = min(ax),min(ay)
    max_x, max_y = max(ax),max(ay)
    x_len, y_len = max_x - min_x + 1, max_y - min_y + 1

    coord = [['.'] * x_len for _ in range(y_len)]

    for star_x,star_y in intersect:
        nx = star_x + abs(star_x) if min_x < 0 else star_x - min_x
        ny = star_y + abs(star_y) if min_y < 0 else star_y - min_y
        complex[ny][nx] = '*'
    
    for result in coord:
        answer.append(''.join(result))
        return answer[::-1]