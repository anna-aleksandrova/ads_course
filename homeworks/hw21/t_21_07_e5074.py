if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        degree = [0 for _ in range(n)]
        for _ in range(m):
            v1, v2 = map(int, f.readline().split())
            degree[v1 - 1] += 1
            degree[v2 - 1] += 1
    for deg in degree:
        print(deg)
