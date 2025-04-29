if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [set() for _ in range(n)]
        for _ in range(m):
            u, v = [int(el) for el in f.readline().split()]
            graph[u-1].add(v)
            graph[v-1].add(u)
        for i in range(n):
            if len(graph[i]) != n - 1:
                print("NO")
                break
        else:
            print("YES")
