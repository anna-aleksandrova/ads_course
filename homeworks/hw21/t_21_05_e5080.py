if __name__ == "__main__":
    res = 0
    with open("input.txt") as f:
        n = int(f.readline())
        for i in range(n):
            deg = 0
            for el in f.readline().split():
                deg += int(el)
            if deg == 1:
                res += 1
    print(res)