from collections import deque

def solve(graph, n):
    colours = [-1 for _ in range(n)]
    while -1 in colours:
        start = colours.index(-1)
        colours[start] = 0
        q = deque()
        q.append(start)
        while q:
            current = q.popleft()
            for neigh in graph[current]:
                if colours[neigh] == colours[current]:
                    return "NO"
                if colours[neigh] == -1:
                    colours[neigh] = (colours[current] + 1) % 2
                    q.append(neigh)
    return "YES"

if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [set() for _ in range(n)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u-1].add(v-1)
            graph[v-1].add(u-1)
    if m == 0:
        print("YES")
    else:
        start = u-1
        print(solve(graph, n))
    