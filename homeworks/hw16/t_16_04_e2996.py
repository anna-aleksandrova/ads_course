min_el: int = 2 ** 64 - 1

class Tree:
    def __init__(self, key: int, data: int, children: [int]):
        self.key = key
        self.data = data
        self.children = []

    def add_children(self, children: [int]):
        for el in children:
            self.children.append(el)

    def get_child(self, key: int):
        if self.key == key:
            return self
        for child in self.children:
            res = child.get_child(key)
            if res:
                return res
        return None

def DFS(tree, _sum):
    global min_el
    if len(tree.children) == 0:
        temp = _sum + tree.data
        if temp < min_el:
            min_el = temp
    for child in tree.children:
        DFS(child, _sum + tree.data)
        
if __name__ == "__main__":
    with open("input.txt") as f:
        N = int(f.readline())
        nodes = {}

        for i in range(1, N + 1):
            nodes[i] = Tree(i, None, [])

        i = 1
        for line in f:
            line = [int(el) for el in line.split()]
            data, am, *children = line
            node = nodes[i]
            node.data = data
            node.add_children([nodes[child] for child in children])
            i += 1

    DFS(nodes[1], 0)
    print(min_el)