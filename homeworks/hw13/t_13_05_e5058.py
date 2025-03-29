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
            raise Exception("Stack: 'pop' applied to empty container") # better to create your own extension -> general rule
        current_top = self.top_node
        item = current_top.item
        self.top_node = self.top_node.next
        return item

def correct(sequence: str):
    stack = Stack()
    corr = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for el in sequence:
        if el in corr.values():
            stack.push(el)
        elif stack.empty():
            return "no"
        elif stack.pop() != corr[el]:
            return "no"
        else:
            pass
    if not stack.empty():
        return "no"
    else:
        return "yes"

if __name__ == "__main__":
    seq = input()
    print(correct(seq))
            