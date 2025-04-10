class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None
        self.prev: [Node | None] = None

class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None
        self.current: [Node | None] = None
        self.size = 0
    
    def empty(self):
        return self.head is None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв’язного Списку"""
        node = Node(val)
        if self.empty():
            self.head = self.current = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
    
    def insert(self, node: Node):
        """Inserts a node after current.
        """
        node.prev = self.current
        node.next = self.current.next
        self.current.next.prev = node
        self.current.next = node
        for i in range(2):
            self.current = self.current.next

    def ReorderList(self) -> None:
        """Перегрупувати елементи списку як наведено вище"""
        for i in range(self.size // 2):
            node = self.tail
            self.tail = node.prev
            self.insert(node)


    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
        node = self.head
        for i in range(self.size):
            print(node.data, end = " ")
            node = node.next

if __name__ == "__main__":
    n = int(input())
    lst = List()
    for el in input().split():
        lst.addToTail(el)
    lst.ReorderList()
    lst.Print()
    print()
    