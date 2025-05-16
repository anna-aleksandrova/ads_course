import sys
sys.setrecursionlimit(10**6)

def dfs(graph: list[set], visited: set[int], start: int, control):
    visited.add(start)
    control[start] = 1
    for neigh in graph[start]:
        if neigh not in visited:
            dfs(graph, visited, neigh, control)
    
def solve(graph: list[set], n):
    control = [0 for i in range(n+1)]
    res = []
    for i in range(1, n+1):
        if control[i] == 0:
            visited = set()
            dfs(graph, visited, i, control)
            res.append(visited)
    print(len(res))
    for component in res:
        print(len(component))
        for vertex in component:
            print(vertex, end = " ")
        print()

if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [set() for i in range(n+1)]
        for i in range(m):
            u, v = map(int, f.readline().split())
            graph[u].add(v)
            graph[v].add(u)
    solve(graph, n)
    