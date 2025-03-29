class Node:

    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:

    def __init__(self):
        self.top_node = None
    
    def empty(self):
        return self.top_node is None
    
    def push(self, item):
        new_node = Node(item)
        if not self.empty():
            new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.empty():
            raise Exception("Stack: 'pop' applied to empty container")
        current_top = self.top_node
        item = current_top.item
        self.top_node = self.top_node.next
        return item

def convert(number: int, base: int):
    stack = Stack()
    while number != 0:
        temp = number % base
        if temp > 9:
            stack.push("[" + str(temp) + "]")
        else:
            stack.push(str(number % base))
        number //= base
    res = ""
    while not stack.empty():
        res += stack.pop()
    return res

if __name__ == "__main__":
    number = int(input())
    base = int(input())
    print(convert(number, base))