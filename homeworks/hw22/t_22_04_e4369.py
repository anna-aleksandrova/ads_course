from collections import deque

def solve(graph, starts, n):
    q = deque()
    distances = {}
    for start in starts:
        q.append(start)
        distances[start] = 0
    
    while q:
        current = q.popleft()
        for neigh in graph[current]:
            if neigh not in distances:
                distances[neigh] = distances[current] + 1
                q.append(neigh)
    
    time = max(distances.values())
    vertex = n
    for key in distances.keys():
        if distances[key] == time and key < vertex:
            vertex = key
    print(time)
    print(vertex)

if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [set() for _ in range(n+1)]
        for i in range(m):
            u, v = map(int, f.readline().split())
            graph[u].add(v)
            graph[v].add(u)
        k = int(f.readline())
        starts = [int(el) for el in f.readline().split()]
    solve(graph, starts, n)