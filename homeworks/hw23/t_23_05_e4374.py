def dfs(graph: list[set], delete: list, visited: set, start: int):
    visited.add(start)
    for neigh in graph[start]:
        if neigh not in visited and {start, neigh} not in delete:
            dfs(graph, delete, visited, neigh)

def solve(graph: list[set], delete: list, n):
    visited = set()
    dfs(graph, delete, visited, 1)
    if len(visited) != n:
        return "Disconnected"
    else:
        return "Connected"


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [set() for _ in range(n+1)]
        edges = {}
        for i in range(m):
            u, v = map(int, f.readline().split())
            graph[u].add(v)
            graph[v].add(u)
            edges[i + 1] = {u, v}
        k = int(f.readline())
        for i in range(k):
            am, *d_edges = map(int, f.readline().split())
            delete = []
            for k in d_edges:
                delete.append(edges[k])
            print(solve(graph, delete, n))


