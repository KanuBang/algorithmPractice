
# ㄱ
def find_max_min(array, low, high):
  if low == high:
    return array[low], array[low] 

  mid = (low + high) // 2
  left_max, left_min = find_max_min(array, low, mid)
  right_max, right_min = find_max_min(array, mid + 1, high)

  return max(left_max, right_max), min(left_min, right_min) 

array = [4,2,3,1]
low = 0
high = len(array)-1

max, min = find_max_min(array,low,high)
print(max, min)
# 위 코드에서
# 인데스를 전달하는 것은 분할ㄴs 
# 재귀호출하여 값을 구하는 것 + max,min은 정복
# return 문은 합병