from PriorityQueue import PriorityQueue
import sys

INF = sys.maxsize


def Dijkstra(graph, n, s, f):
    distances = [INF for _ in range(n+1)]
    distances[s] = 0
    pq = PriorityQueue()
    pq.insert(s, 0)
    while not pq.empty():
        v = pq.extractMinimum()
        for u in range(1, n+1):
            if graph[v-1][u-1] != -1:
                if distances[u] > distances[v] + graph[v-1][u-1]:
                    distances[u] = distances[v] + graph[v-1][u-1]
                    if u in pq:
                        pq.updatePriority(u, distances[u])
                    else:
                        pq.insert(u, distances[u])
    res = distances[f]
    if res == INF:
        return -1
    else:
        return res


if __name__ == "__main__":
    with open("input.txt") as file:
        n, s, f = map(int, file.readline().split())
        graph = []
        for _ in range(n):
            row = [int(el) for el in file.readline().split()]
            graph.append(row)
    print(Dijkstra(graph, n, s, f))