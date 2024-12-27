# from collections import deque

# stack = deque()

# stack.append(1)
# stack.append('a')
# # print(stack.count(stack))
# # stack.pop()
# stack.appendleft(0)
# print(stack)



# print(f'Stack: {stack}')
# print(f'Top element: {stack[-1]}')

# print(f'Stack output as a list: {list(stack)}')

# print(f'Is Stack Empty? {len(stack) == 0}')
# print(f'Len of Stack: {len(stack)}')


# stack.pop()
# print(stack)
# stack.popleft()
# print(stack)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\9_stack.py
# deque([0, 1, 'a'])
# Stack: deque([0, 1, 'a'])
# Top element: a
# Stack output as a list: [0, 1, 'a']
# Is Stack Empty? False
# Len of Stack: 3
# deque([0, 1])
# deque([1])




from queue import LifoQueue

stack = LifoQueue()

print(f'Is stack full? {stack.full()}')