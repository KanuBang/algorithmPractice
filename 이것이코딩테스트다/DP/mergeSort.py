def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    print(f'mid: {mid} low_arr: {low_arr}, high_arr: {high_arr}')
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    print(f'after while {merged_arr}')

    print(f'l: {l}, low_arr[l:]: {low_arr[l:]}')
    merged_arr += low_arr[l:]
    print(f'after low_arr merged: {merged_arr}')

    print(f'h: {h}, high_arr[h:]: {high_arr[h:]}')
    merged_arr += high_arr[h:]
    print(f'after high_arr merged: {merged_arr}')
    print()
    return merged_arr

arr = [0,4,2,3,1]
sortedArr =merge_sort(arr)
print(sortedArr)

