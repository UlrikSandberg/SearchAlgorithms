from collections import deque

#Stack - LIFO

#Initialize stack
stack = ["a", "b", "c"]

stack.append("e")

print stack

print stack.pop()

print stack

print stack.pop()

print stack

stack.append("d")
print stack

#Que - FIFO

#Initialze que

dq = deque(["b", "c", "D"])

dq.append("e")
print dq

dq.appendleft("a")
print dq


