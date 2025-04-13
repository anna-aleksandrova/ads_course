class BinarySearchTree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        while True:
            if node.key > value:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = BinarySearchTree(value)
                    break
            else:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = BinarySearchTree(value)
                    break
    
    def has_children(self):
        return self.left is not None or self.right is not None

def solve(sequence: list):
    Tree = BinarySearchTree(sequence[0])
    for el in sequence[1:]:
        Tree.insert(el)
    i = 1
    node = Tree
    while node.has_children():
        curr = sequence[i]
        if curr < node.key:
            if node.left.key != curr:
                return "NO"
            else:
                node = node.left
        elif curr > node.key:
            if node.right.key != curr:
                return "NO"
            else:
                node = node.right
        i += 1
    if len(sequence) > i:
        return "NO"
    return "YES"

if __name__ == "__main__":
    with open("input.txt") as f:
        sequence = []
        for line in f:
            for el in line.split():
                sequence.append(int(el))
    print(solve(sequence))

    
        
