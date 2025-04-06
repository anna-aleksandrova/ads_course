class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None
        self.prev: [Node | None] = None
    
class List:
    """Doubly linked list."""
    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None
    
    def empty(self):
        return self.head is None
    
    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв’язного Списку"""
        node = Node(val)
        if self.empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
        node = self.head
        while node is not None:
            print(node.data, end = " ")
            node = node.next

    def PrintReverse(self) -> None:
        """Вивести елементи Зв’язного Списку в зворотному порядку"""
        node = self.tail
        while node is not None:
            print(node.data, end = " ")
            node = node.prev

if __name__ == "__main__":
    _ = int(input())
    lst = List()
    for el in input().split():
        lst.addToTail(el)
    lst.Print()
    print()
    lst.PrintReverse()