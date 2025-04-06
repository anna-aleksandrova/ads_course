class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None

class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None
        self.size = 0

    def empty(self):
        return self.head is None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв’язного Списку"""
        node = Node(val)
        if self.empty():
            self.head  = self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
        self.size += 1

    def RotateRight(self, k: int) -> None:
        """Здійснити обертання Зв’язного Списку праворуч на k позицій"""
        k = k % self.size
        for i in range(self.size - k):
            self.head = self.head.next
            self.tail= self.tail.next

    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
        node = self.head
        while True:
            print(node.data, end = " ")
            node = node.next
            if node == self.head:
                break
    
if __name__ == "__main__":
    with open("input.txt") as f:
        _ = int(f.readline())
        lst = List()
        data = f.readline().split()
        for el in data:
            lst.addToTail(int(el))
        for line in f:
            line = line.strip()
            if line:
                k = int(line)
                lst.RotateRight(k)
                lst.Print()
                print()
            

