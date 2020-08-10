
class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):

    def __init__(self):
        self.stack_obj = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack_obj.push(item)
        if not self.max_stack.peek() or item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        item = self.stack_obj.pop()
        if item == self.max_stack.peek():
            self.max_stack.pop()
        return item

    def get_max(self):
        return self.max_stack.peek()
