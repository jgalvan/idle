class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return None

    def peek_next_to_last(self):
        if self.size() > 1:
            return self.items[len(self.items)-2]
        else:
            return None

    def size(self):
        return len(self.items)