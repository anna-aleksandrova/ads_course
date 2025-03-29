class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None
    
class Deque:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def empty(self):
        return self._front is None

    def push_front(self, item):
        node = Node(item)
        node.next = self._front
        if self.empty():
            self._back = node
        else:
            self._front.prev = node
        self._front = node
        self._size += 1
        return "ok"
    
    def push_back(self, item):
        node = Node(item)
        node.prev = self._back
        if self.empty():
            self._front = node
        else:
            self._back.next = node
        self._back = node
        self._size += 1
        return "ok"
    
    def pop_front(self):
        if self.empty():
            return "error"
        res = self._front.item
        self._front = self._front.next
        if self._front is None:
            self._back = None
        else:
            self._front.prev = None
        self._size -= 1
        return res
    
    def pop_back(self):
        if self.empty():
            return "error"
        res = self._back.item
        self._back = self._back.prev
        if self._back is None:
            self._front = None
        else:
            self._back.next = None
        self._size -= 1
        return res
    
    def front(self):
        if self.empty():
            return "error"
        return self._front.item
    
    def back(self):
        if self.empty():
            return "error"
        return self._back.item
    
    def size(self):
        return self._size
    
    def clear(self):
        self._front = None
        self._back = None
        self._size = 0
        return "ok"
    
    def exit(self):
        return "bye"
    
    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)
    
if __name__ == "__main__":
    deque = Deque()
    with open("input.txt") as f:
        for line in f:
            res = deque.execute(line)
            print(res)
            if res == "bye":
                break