array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j

    # 가장 앞에 것과 범위에서 가장 작은 값을 스와핑
    array[i], array[min_index] = array[min_index],array[i]
    print(array)

print(array)

'''
선택정렬에서 선택은 가장 작은 것을 선택한다는 의미이다.
매번 한 텀에서 가장 앞의 요소와 범위에서 가장 작은 값을 스와핑한다.
시간복잡도는 O(N^2) 이다.
'''