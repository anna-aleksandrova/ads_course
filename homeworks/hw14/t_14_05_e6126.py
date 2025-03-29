class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0
    
    def empty(self):
        return self._front is None
    
    def push(self, item):
        node = Node(item)
        if self.empty():
            self._front = node
        else:
            self._back.next = node
        self._back = node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        res = self._front.item
        self._front = self._front.next
        if self._front is None:
            self._back = None
        self._size -= 1
        return res
    
    def front(self):
        if self.empty():
            return "error"
        return self._front.item
    
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
    queue = Queue()
    with open("input.txt") as f:
        for line in f:
            res = queue.execute(line)
            print(res)
            if res == "bye":
                break