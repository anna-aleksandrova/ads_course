import sys
INF = sys.maxsize

class Disjoint_Set:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
    
    def find(self, x):
        while self.parents[x] != x:
            x = self.parents[x]
        return x
    
    def union(self, u, v):
        U, V = self.find(u), self.find(v)
        if U != V:
            self.parents[V] = U
            return True
        else:
            return False
        
def sort_edges(edges: list[tuple[int]]):
    if len(edges) > 1:
        mid = len(edges) // 2
        lefthalf = edges[:mid]
        righthalf = edges[mid:]

        sort_edges(lefthalf)
        sort_edges(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][2] < righthalf[j][2]:
                edges[k] = lefthalf[i]
                i += 1
            else:
                edges[k] = righthalf[j]
                j += 1
            k += 1
        
        while i < len(lefthalf):
            edges[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            edges[k] = righthalf[j]
            j += 1
            k += 1


def kruskal(edges: list[tuple[int]], n: int, banned=None):
    """Returns the weight of the MST of G.
    """
    T = set()
    MST_weight = 0
    edge_count = 0
    if banned is None:
        sort_edges(edges)
    ds = Disjoint_Set(n)
    for edge in edges:
        if edge == banned:
            continue
        u, v, w = edge
        if ds.union(u, v):
            T.add(edge)
            edge_count += 1
            MST_weight += w
            if edge_count == n - 1:
                break
    if edge_count == n - 1:
        return T, MST_weight
    else:
        return set(), INF

def SBMST(edges: list[tuple[int]], T: set, n: int):
    res = INF
    for edge in T:
        _, temp = kruskal(edges, n, edge)
        if temp < res:
            res = temp
    return res

if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [{} for _ in range(n+1)]
        edges = []
        for _ in range(m):
            a, b, w = map(int, f.readline().split())
            edges.append((a, b, w))
    MST, wMST = kruskal(edges, n)
    print(wMST, SBMST(edges, MST, n))
