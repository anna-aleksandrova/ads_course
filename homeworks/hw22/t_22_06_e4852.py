from collections import deque

def solve(graph, start, n):
    q = deque()
    q.append(start)
    distances = [-1 for _ in range(n)]
    distances[start] = 0

    while q:
        current = q.popleft()
        for i in range(n):
            if graph[current][i] == 1 and distances[i] == -1:
                distances[i] = distances[current] + 1
                q.append(i)
    print(*distances)

if __name__ == "__main__":
    with open("input.txt") as f:
        n, start = map(int, f.readline().split())
        graph = [
            [int(el) for el in f.readline().split()] for _ in range(n)
        ]
    solve(graph, start - 1, n)
