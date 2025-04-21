class PriorityQueue:
    def __init__(self):
        self.items = [["0", 0]]
        self.size = 0
        self.map = {}

    def max_child(self, left, right):
        if right > self.size:
            return left
        else:
            if self.items[left][1] > self.items[right][1]:
                return left
            else:
                return right
    
    def swap(self, i, j):
        """Swap elements with indexes <i>, <j> in <self.items>.
        """
        key_i = self.items[i][0]
        key_j = self.items[j][0]
        self.map[key_i] = j
        self.map[key_j] = i
        self.items[i], self.items[j] = self.items[j], self.items[i]


    def siftUp(self):
        i = self.size
        while i > 1:
            parent = i // 2
            if self.items[parent][1] < self.items[i][1]:
                self.swap(parent, i)
            else:
                break
            i = parent
    
    def siftDown(self):
        i = 1
        while 2*i < self.size + 1:
            left = 2*i
            right = 2*i + 1
            max_child = self.max_child(left, right)
            if self.items[i][1] < self.items[max_child][1]:
                self.swap(max_child, i)
            else:
                break
            i = max_child
    
    def add(self, id: str, priority: int):
        self.items.append([id, priority])
        self.size += 1
        self.map[id] = self.size
        self.siftUp()
    
    def pop(self):
        res = self.items[1]
        self.swap(1, -1)
        self.items.pop()
        self.size -= 1
        self.siftDown()
        return res
    
    def change(self, id, priority):
        i = self.map[id]
        old_priority = self.items[i][1]
        self.items[i][1] = priority
        if priority > old_priority:
            while i > 1:
                parent = i // 2
                if self.items[parent][1] < self.items[i][1]:
                    self.swap(parent, i)
                else:
                    break
                i = parent
        else:
            while 2 * i <= self.size:
                left = 2 * i
                right = 2 * i + 1
                max_child = self.max_child(left, right)
                if self.items[i][1] < self.items[max_child][1]:
                    self.swap(i, max_child)
                else:
                    break
                i = max_child

if __name__ == "__main__":
    pq = PriorityQueue()
    with open("input.txt") as f:
        for line in f:
            cmd, *args = line.split()
            if cmd == "ADD":
                pq.add(args[0], int(args[1]))
            elif cmd == "POP":
                print(*pq.pop())
            elif cmd == "CHANGE":
                pq.change(args[0], int(args[1]))

