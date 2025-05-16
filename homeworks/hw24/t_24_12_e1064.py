from collections import deque

def solve(matrix: list[list[str]], n: int, start, end):
    di = [-1, 1, 2, 2, 1, -1, -2, -2]
    dj = [-2, -2, -1, 1, 2, 2, 1, -1]

    wave = [[-1 for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append(start)
    wave[start[0]][start[1]] = 0
    exists = False
    while queue:
        current = queue.popleft()
        for k in range(len(di)):
            i = current[0] + di[k]
            j = current[1] + dj[k]
            if -1 < i < n and -1 < j < n:
                if wave[i][j] == -1 and matrix[i][j] != "#":
                    wave[i][j] = wave[current[0]][current[1]] + 1
                    queue.append((i, j))
            if (i, j) == end:
                exists = True
                break
    if exists:
        current = end
        while current != start:
            for k in range(len(di)):
                i = current[0] + di[k]
                j = current[1] + dj[k]
                if -1 < i < n and -1 < j < n:
                    if wave[i][j] == wave[current[0]][current[1]] - 1:
                        matrix[i][j] = "@"
                        current = (i, j)
                        break
        return "Possible"
    else:
        return "Impossible"

def show(matrix):
    for row in matrix:
        print("".join(row))

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        matrix = []
        start = None
        for i in range(n):
            line = f.readline().strip()
            row = []
            for j in range(n):
                if line[j] == "@" and start is None:
                    start = (i, j)
                if line[j] == "@" and start is not None:
                    end = (i, j)
                row.append(line[j])
            matrix.append(row)
    res = solve(matrix, n, start, end)
    if res == "Impossible":
        print(res)
    else:
        show(matrix)

