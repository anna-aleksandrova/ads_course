from collections import deque

def solve(matrix, n, start, end):
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]
    wave = [
        [-1 for _ in range(n+2)] for _ in range(n+2)
    ]
    wave[start[0]][start[1]] = 0
    queue = deque()
    queue.append(start)
    exists = False
    while queue:
        current = queue.popleft()
        for k in range(len(di)):
            i = current[0] + di[k]
            j = current[1] + dj[k]
            if matrix[i][j] != "O" and matrix[i][j] is not None and wave[i][j] == -1:
                wave[i][j] = wave[current[0]][current[1]] + 1
                queue.append((i, j))
            if (i, j) == end:
                exists = True
                break
    if exists:
        current = end
        while True:
            if current == start:
                break
            matrix[current[0]][current[1]] = "+"
            for k in range(len(di)):
                i = current[0] + di[k]
                j = current[1] + dj[k]
                if wave[i][j] == wave[current[0]][current[1]] - 1:
                    current = (i, j)
                    break
        return "Y"
    else:
        return "N"


def show(matrix):
    for row in matrix[1:-1]:
        for el in row:
            if el is not None:
                print(el, end="")
        print()

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        maze = [
            [None for _ in range(n+2)]
        ]
        for i in range(n):
            row = [None]
            line = f.readline().strip()
            for j in range(len(line)):
                if line[j] == "@":
                    start = (i+1, j+1)
                if line[j] == "X":
                    end = (i+1, j+1)
                row.append(line[j])
            row.append(None)
            maze.append(row)
        maze.append([None for _ in range(n+2)])
    res = solve(maze, n, start, end)
    print(res)
    if res == "Y":
        show(maze)
