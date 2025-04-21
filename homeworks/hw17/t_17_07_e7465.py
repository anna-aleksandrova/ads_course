class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, head):
        self.head = head
    
    def Insert(self, val: int):
        node = self.head
        while True:
            if node.val > val:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            else:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break

    def IsSameTree(self, p):
        pass

def DFS(tree, res: list):
    res.append(tree.val)
    if tree.left is not None:
        DFS(tree.left, res)
    if tree.right is not None:
        DFS(tree.right, res)


def solve(tree1: list, tree2: list):
    Tree1 = Tree(TreeNode(tree1[0]))
    for el in tree1[1:]:
        Tree1.Insert(el)
    Tree2 = Tree(TreeNode(tree2[0]))
    for el in tree2[1:]:
        Tree2.Insert(el)
    res1 = []
    res2 = []
    DFS(Tree1.head, res1)
    DFS(Tree2.head, res2)
    return res1 == res2

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        tree1 = [int(el) for el in f.readline().split()]
        m = int(f.readline())
        tree2 = [int(el) for el in f.readline().split()]
        print(int(solve(tree1, tree2)))
    
