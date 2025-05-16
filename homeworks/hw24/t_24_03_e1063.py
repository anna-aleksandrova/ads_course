from collections import deque

def solve(matrix, m, n):
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]
    wave = [
        [-1 for _ in range(n+2)] for _ in range(m+2)
    ]
    res = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if wave[i][j] == -1 and matrix[i][j] == "#":
                wave[i][j] = 0
                queue = deque()
                queue.append((i, j))
                while queue:
                    current = queue.popleft()
                    for k in range(len(di)):
                        _i = current[0] + di[k]
                        _j = current[1] + dj[k]
                        if matrix[_i][_j] != "." and matrix[_i][_j] is not None and wave[_i][_j] == -1:
                            wave[_i][_j] = wave[current[0]][current[1]] + 1
                            queue.append((_i, _j))
                res += 1
    return res

if __name__ == "__main__":
    with open("input.txt") as f:
        m, n = map(int, f.readline().split())
        maze = [
            [None for _ in range(n+2)]
        ]
        for i in range(m):
            row = [None]
            line = f.readline().strip()
            for j in range(len(line)):
                row.append(line[j])
            row.append(None)
            maze.append(row)
        maze.append([None for _ in range(n+2)])
    res = solve(maze, m, n)
    print(res)
