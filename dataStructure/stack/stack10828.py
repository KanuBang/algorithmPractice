import sys
input = sys.stdin.readline
n = int(input())
order = ""
top = -1
size = 0
stack = []
ans =[ ]

while n > 0:
    order = input().rstrip()
    orderCase = order[0]
    if orderCase == 'p':
        #push
        if order[1] == 'u':
            stack.append(int(order[4:]))
            size += 1
            top += 1
        #pop
        else:
            if size == 0:
                ans.append(-1)
            else:
                ans.append(stack.pop())
                top -= 1
                size -= 1

    else:
        #top
        if orderCase == 't':
            if size == 0:
                ans.append(-1)
            else:
                ans.append(stack[top])

        #size
        elif orderCase == 's':
            ans.append(size)

        #empty
        else:
            if size == 0:
                ans.append(1)
            else:
                ans.append(0)

    n -= 1


for i in ans:
    print(i)

