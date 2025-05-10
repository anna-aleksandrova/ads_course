def dfs_kosaraju(graph: list[set[int]], stack: list, visited: set, start: int):
    visited.add(start)
    for neigh in graph[start]:
        if neigh not in visited:
            dfs_kosaraju(graph, stack, visited, neigh)
    stack.append(start)

def dfs(graph: list[set[int]], visited: set, start: int):
    visited.add(start)
    for neigh in graph[start]:
        if neigh not in visited:
            dfs(graph, visited, neigh)


def solve(graph: list[set[int]], graph_transpose: list[set[int]]):
    visited = set()
    stack = []
    for i in range(1, n+1):
        if i not in visited:
            dfs_kosaraju(graph, stack, visited, i)
    visited = set()
    res = 0
    while stack:
        i = stack.pop()
        if i not in visited:
            dfs(graph_transpose, visited, i)
            res += 1
    return res


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [set() for i in range(n+1)]
        graph_transpose = [set() for i in range(n+1)]
        for i in range(m):
            u, v = map(int, f.readline().split())
            graph[u].add(v)
            graph_transpose[v].add(u)
    print(solve(graph, graph_transpose))
    