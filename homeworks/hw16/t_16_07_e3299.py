class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        return self.front is None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.empty():
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node

    def dequeue(self):
        if self.empty():
            raise Exception("Queue: applied to empty container")
        current_front = self.front
        item = current_front.item
        self.front = self.front.next
        del current_front

        if self.front is None:
            self.back = None
        return item

class Tree:
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.children = []

    def bfs(self, key, came_from=None):
        queue = Queue()
        queue.enqueue(self)
        while not queue.empty():
            node = queue.dequeue()
            if node is came_from:
                continue
            if node.key == key:
                return node
            for child in node.children:
                queue.enqueue(child)
        return None

    def lca(self, i, j):
        node = self.bfs(i)
        came_from = None
        while True:
            if node.bfs(j, came_from) is not None:
                return node.key
            came_from = node
            node = node.parent
    
    def __repr__(self):
        temp = f"""
Tree: key = {self.key}, children = {self.children}
        """
        return temp

def build_tree(nodes, n):
    """
    Args:
        nodes (list): nodes[i] is the key of (i+1)th vertex parent; len(nodes) = n-1.
        n (int): The amount of nodes in the tree.
    
    Returns:
        tree (Tree): A correctly built tree.
    """
    _nodes = {}
    for i in range(n):
        _nodes[i] = Tree(i)
    for i in range(n-1):
        nparent_ip1 = nodes[i]
        _nodes[i+1].parent = _nodes[nparent_ip1]
        _nodes[nparent_ip1].children.append(_nodes[i+1])
    return _nodes[0]
        
def dfs(tree):
    for child in tree.children:
        dfs(child)

def gen(a1, a2, n, m, x, y, z):
    res = [a1, a2]
    for i in range(2, 2*m):
        res.append((x*res[i-2] + y*res[i-1] + z) % n)
    return res

def solve(tree: Tree, n, m, a1, a2, x, y, z):
    res = 0
    v = 0
    a = gen(a1, a2, n, m, x, y, z)
    for i in range(1, m+1):
        v = tree.lca((a[2*i-2]+v)%n, a[2*i-1])
        res += v
    return res

if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = [int(el) for el in f.readline().split()]
        nodes = [int(node) for node in f.readline().split()]
        tree = build_tree(nodes, n)
        a1, a2 = [int(el) for el in f.readline().split()]
        x, y, z = [int(el) for el in f.readline().split()]
    print(solve(tree, n, m, a1, a2, x, y, z))
        