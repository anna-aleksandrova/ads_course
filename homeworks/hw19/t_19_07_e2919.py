def calc_p(tree, i, n):
    if tree[i][0] == -1 or tree[i][1] == -1:
        return 1
    else:
        return 1 + min(calc_p(tree, tree[i][0], n), calc_p(tree, tree[i][1], n))

def solve(tree, potentials):
    for i in range(1, n + 1):
        if tree[i][0] == -1 and tree[i][1] != -1:
            return i
        if potentials[tree[i][0]] < potentials[tree[i][1]]:
            return i
    return -1

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        tree = [None for _ in range(n+1)]
        potentials = [None for _ in range(n+1)]
        for i in range(1, n+1):
            left, right = map(int, f.readline().split())
            tree[i] = (left, right)
    for i in range(n, 0, -1):
        potentials[i] = calc_p(tree, i, n)
    print(solve(tree, potentials))
