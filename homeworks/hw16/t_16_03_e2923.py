class Tree:
    def __init__(self, key: int, colour: int):
        self.key = key
        self.colours = set()
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def solve(nodes: dict, N):
    for i in range(1, N+1):
        print(len(nodes[i].colours), end = " ")
    
if __name__ == "__main__":
    with open("input.txt") as f:
        N = int(f.readline())
        
        nodes = {}
        for i in range(1, N+1):
            nodes[i] = Tree(i, 0)
        
        i = 1
        for line in f:
            parent, colour = [int(el) for el in line.split()]
            node = nodes[i]
            node.colours.add(colour)
            if parent == 0:
                i_root = i
            else:
                par_node = nodes[parent]
                node.parent = par_node
                par_node.add_child(node)
                while node.parent is not None:
                    node.parent.colours.add(colour)
                    node = node.parent
            i += 1
    root = nodes[i_root]
    solve(nodes, N)
        