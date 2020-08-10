"""Implement a new class MaxStack with a method get_max()
 that returns the largest element in the stack. get_max()
 should not remove the item.

Your stacks will contain only integers
"""


# class Stack(object):

#     def __init__(self):
#         """Initialize an empty stack"""
#         self.items = []

#     def push(self, item):
#         """Push a new item onto the stack"""
#         self.items.append(item)

#     def pop(self):
#         """Remove and return the last item"""
#         # If the stack is empty, return None
#         # (it would also be reasonable to throw an exception)
#         if not self.items:
#             return None

#         return self.items.pop()

#     def peek(self):
#         """Return the last item without removing it"""
#         if not self.items:
#             return None
#         return self.items[-1]


# class MaxStack(object):

#     # Implement the push, pop, and get_max methods
#     def __init__(self):
#         self.stack_obj = Stack()
#         self.max_stack = Stack()

#     def push(self, item):
#         self.stack_obj.push(item)
#         if not self.max_stack.peek() or item >= self.max_stack.peek():
#             self.max_stack.push(item)

#     def pop(self):
#         item = self.stack_obj.pop()
#         if item == self.max_stack.peek():
#             self.max_stack.pop()
#         return item

#     def get_max(self):
#         return self.max_stack.peek()
