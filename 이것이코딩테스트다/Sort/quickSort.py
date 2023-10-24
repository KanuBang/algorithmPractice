array = [0,4,2,3,1]

def quick_sort(array, start, end): 

    if start >= end: # 원소가 1개이면 바로 종료
        return
    
    pivot = start # 호어 분할
    left = start+1 # +1 되면서 왼쪽으로 진행, pivot보다 큰 수를 찾음
    right = end # -1 되면서 오른쪽으로 진행, pivot보다 작은 수를 찾음
    print(f'pivot: {pivot}, start: {start}, right:{end}')
    # left와 right이 엇갈리면, right의 Pivot보다 작은 수와 pivot이 swaping 된다. 이때, 배열은 pivot으로 이중분할 된다.
    # 이중분할 되면 pivot의 왼쪽과 오른쪽을 따로 퀵정렬 한다.
    while left <= right:
        print(f'before: {array}')
        # 왼쪽으로 진행하며 pivot보다 큰 수를 찾는다
        # while문을 돌며 left가 + 1 씩 증가한다는 의미 = pivot보다 큰 수를 아직 찾지 못했다.
        # while문을 탈출한다면, 
        # 1) pivot보다 큰 수를 찾았다. 그 큰 수의 index는 left다.
        # 2) 탐색하다가 끝에 도달하여, 이동할 때가 없다.
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        # 오른쪽으로 진행하며, pivot보다 작은 수를 찾는다.
        # while문을 돌며 right이 -1 씩 감소한다는 의미 = pivot보다 작은 수를 아직 찾지 못했다.
        # while문을 탈출한다면,
        # 1) pivot보다 작은 수를 찾았다. 그 작은 수의 Index는 right이다.
        # 2) 탐색하다가 start에 도달하여 이동할때가 없다.
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        # pivot보다 큰 수, 작은 수를 찾고 난 후

        # 만약, 왼쪽 진행 방향과 오른쪽 진행 방향이 엇갈렸다면, 오른쪽 진행방향이 찾은 pivot 보다 작은 수와 pivot를 swaping 한다.
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        
        # 진행방향이 엇갈리지 않았다면, pivot 보다 작은 수와 큰 수를 swap 한다.
        else:
            array[left], array[right] = array[right], array[left]
        
        print(f'left{left},right{right}')
        print(f'after{array}')
        print()

    print(f'start: {start}')
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)        


quick_sort(array,0,len(array)-1)
print(array)