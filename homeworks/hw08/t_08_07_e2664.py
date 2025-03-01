def solve(array):
    n = len(array)
    for pos in range(n):
        flag = True
        x = array[pos]
        while pos > 0:
            if array[pos - 1] <= x:
                break
            else:
                array[pos] = array[pos - 1]
            pos -= 1
            flag = False
        array[pos] = x
        if not flag:
            print(" ".join(map(str, array)))

if __name__ == "__main__":
    am = int(input())
    array = [int(el) for el in input().split()]
    solve(array)