import sys
sys.setrecursionlimit(10**6)
flag: int = 1  # 1 if graph can be topologically sorted, 0 otherwise

def dfs_modified(graph: list[set], colours: list, start: int, stack: list):
    global flag
    if colours[start] == 2 or flag == 0:
        return
    if colours[start] == 1:
        flag = 0
        return
    colours[start] = 1
    for neigh in graph[start]:
        dfs_modified(graph, colours, neigh, stack)
    colours[start] = 2
    stack.append(start)

def topological_sort(graph: list[set], colours: list, n: int):
    global flag
    stack = []
    for i in range(1, n+1):
        dfs_modified(graph, colours, i, stack)
        if flag == 0:
            return "-1"
    res = ""
    while stack:
        res += str(stack.pop()) + " "
    return res
    
if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [set() for i in range(n+1)]
        for i in range(m):
            u, v = map(int, f.readline().split())
            graph[u].add(v)
    colours = [0 for i in range(n+1)]
    print(topological_sort(graph, colours, n))
