from collections import deque

# 큐를 구현하기 위해 deque 라이브러리를 사용한다.
queue = deque()
# 5(삽입) 2(삽입) 3(삽입) 7(삽입) 삭제 1(삽입) 4(삽입) 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
