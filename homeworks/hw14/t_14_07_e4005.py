const: int = 2 * 10 ** 5

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

    def pop(self):
        if self.empty():
            raise Exception("Can't apply 'pop' to an empty queue.")
        res = self._front.item
        self._front = self._front.next
        if self._front is None:
            self._back = None
        self._size -= 1
        return res
    
    def front(self):
        if self.empty():
            raise Exception("Can't apply 'front' to an empty queue.")
        return self._front.item
    
    def size(self):
        return self._size
    
    def clear(self):
        self._front = None
        self._back = None
        self._size = 0

def solve(n: int, p1: list[int], p2: list[int]):
    queue1 = Queue()
    queue2 = Queue()
    for el in p1:
        queue1.push(el)
    for el in p2:
        queue2.push(el)
    counter = 0
    while True:
        if queue1.empty():
            return "second", counter
        if queue2.empty():
            return "first", counter
        if counter == const:
            return None, None
        card1 = queue1.pop()
        card2 = queue2.pop()
        if card1 == 0 and card2 == n-1:
            queue1.push(card1)
            queue1.push(card2)
        elif card1 == n-1 and card2 == 0 :
            queue2.push(card1)
            queue2.push(card2)
        elif card1 > card2:
            queue1.push(card1)
            queue1.push(card2)
        elif card2 > card1:
            queue2.push(card1)
            queue2.push(card2)
        else:
            pass
        counter += 1

if __name__ == "__main__":
    n = int(input())
    p1 = [int(el) for el in input().split()]
    p2 = [int(el) for el in input().split()]
    res = solve(n, p1, p2)
    if res[0] is not None and res[1] is not None:
        print(res[0], res[1])
    else:
        print("draw")
