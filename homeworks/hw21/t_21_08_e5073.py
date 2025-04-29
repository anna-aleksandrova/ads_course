if __name__ == "__main__":
    edges = set()
    flag = 0
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        for _ in range(m+1):
            line = f.readline().strip()
            if line in edges:
                flag = 1
                break
            else:
                edges.add(line)
    if flag:
        print("YES")
    else:
        print("NO")