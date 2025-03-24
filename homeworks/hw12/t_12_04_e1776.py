class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack():

    def __init__(self):
        self._top = None
        self._size = 0

    def empty(self):
        return self._size == 0

    def push(self, item):
        node = Node(item)
        node.next = self._top
        self._top = node
        self._size += 1
        return "ok"
    
    def pop(self):
        if self.empty():
            return "error"
        res = self._top.item
        self._top = self._top.next
        self._size -= 1
        return res
    
    def back(self):
        if self.empty():
            return 0
        return self._top.item

def solve(n, config):
    stack = Stack()
    current = 1
    for el in config:
        while current < n + 1 and (stack._size == 0 or stack.back() != el):
            stack.push(current)
            current += 1
        if stack._size > 0 and stack.back() == el:
            stack.pop()
        else:
            return "No"
    return "Yes"
        

if __name__ == "__main__":
    with open("input.txt") as f:
        while True:
            n = int(f.readline())
            if n == 0:
                break
            while True:
                aux = f.readline()
                if len(aux.split()) != n:
                    print(" ")
                    break
                else:
                    config = [int(el) for el in aux.split()]
                    print(solve(n, config))
