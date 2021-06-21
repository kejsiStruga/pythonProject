"""LIFO -> Last In First Out"""


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        # build in function in python for inserting elements in list
        self.items.append(item)

    def pop(self):
        # this will return the top element of the stack
        self.items.pop()

    def is_empty(self):
        return self.items == []

    def peeK(self):
        if not self.is_empty():
            # returns the last element of the list
            return self.items[-1]

    def get_stack(self):
        return self.items


if __name__ == '__main__':
    s = Stack()
    s.push("A")
    s.push("B")
    print(s.get_stack())
    s.push("C")
    s.pop()
    print(s.get_stack())
    print(s.peeK())
