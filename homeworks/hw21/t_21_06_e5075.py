if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        out_degree = [0 for _ in range(n)]
        in_degree = [0 for _ in range(n)]
        for _ in range(m):
            _out, _in = map(int, f.readline().split())
            out_degree[_out - 1] += 1
            in_degree[_in - 1] += 1
    for _in, _out in zip(in_degree, out_degree):
        print(f"{_in} {_out}")
