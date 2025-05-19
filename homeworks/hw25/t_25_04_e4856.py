import sys
INF = sys.maxsize

def bellman_ford(graph, n, s, f):
    distances = [INF for _ in range(n+1)]
    distances[s] = 0
    predecessor = [None for _ in range(n+1)]
    for i in range(n-1):
        flag = True
        for v in range(1, n+1):
            for neigh in graph[v]:
                if distances[v] + graph[v][neigh] < distances[neigh]:
                    flag = False
                    distances[neigh] = distances[v] + graph[v][neigh]
                    predecessor[neigh] = v
        if flag:
            break
    if distances[f] == sys.maxsize:
        return -1, None
    else:
        i = f
        path = [f]
        while predecessor[i] is not None:
            path.append(predecessor[i])
            i = predecessor[i]
        path.reverse()
        return distances[f], path
        

if __name__ == "__main__":
    with open("input.txt") as file:
        n, m = map(int, file.readline().split())
        s, f = map(int, file.readline().split())
        graph = [{} for _ in range(n+1)]
        for i in range(1, m+1):
            u, v, w = map(int, file.readline().split())
            graph[u][v] = w
            graph[v][u] = w
    length, path = bellman_ford(graph, n, s, f)
    print(length)
    if path:
        print(*path)
    
