def solution(rows, columns, queries):
    answer = []
    # 행렬 생성
    mat = [[] for _ in range(rows)]
    num = 1
    for row in mat:
        for _ in range(columns):
            row.append(num)
            num += 1
    
    #이동 방향: 오른쪽 -> 아래 -> 왼쪽 -> 위
    for q in queries:
        move = []  
        step_col = q[3] - q[1]
        step_row = q[2] - q[0]
        y = q[0] - 1
        x = q[1] - 1
        move.append(mat[y][x])
        
        for c in range(step_col):
            tmp = mat[y][x+1]
            mat[y][x+1] = move[-1]
            move.append(tmp)
            x += 1

        for r in range(step_row):
            tmp = mat[y+1][x]
            mat[y+1][x] = move[-1]
            move.append(tmp)
            y += 1
        
        for c in range(step_col):
            tmp = mat[y][x-1]
            mat[y][x-1] = move[-1]
            move.append(tmp)
            x -= 1
        
        for r in range(step_row):
            tmp = mat[y-1][x]
            mat[y-1][x] = move[-1]
            move.append(tmp)
            y -= 1
        
        answer.append(min(move))
        
    return answer