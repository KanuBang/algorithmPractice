import sys
from collections import deque

input = sys.stdin.readline

numberOfOperands = int(input())
expression = deque(list(input().rstrip()))
valueMap = {}
for i in range(numberOfOperands):
    valueMap[chr(i+65)] = int(input())

def calculate(operator, operand1, operand2):

    if operator == '*':
        return operand1 * operand2
    
    elif operator == '+':
        return operand1 + operand2
    
    elif operator == '-':
        return operand1 - operand2
    
    elif operator == '/':
        return operand1 / operand2

stack = []    
for i in range(len(expression)):
    current = expression.popleft()

    if current not in ['*','+','-','/']:
        stack.append(current)
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
        operator = current
        
        if operand1 in [chr(i) for i in range(65, 91)]:
            operand1 = valueMap[operand1]
        if operand2 in [chr(i) for i in range(65, 91)]:
            operand2 = valueMap[operand2]

        stack.append(calculate(operator,operand1,operand2))

print('{:.02f}'.format(stack[0]))
