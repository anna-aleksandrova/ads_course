def solve(array):
    """The number of swaps in bubble sort.
    """
    n = len(array)
    count = 0
    for j in range(1, n):
        for i in range(n - j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count += 1
    return count

if __name__ == "__main__":
    length = int(input())
    array = [int(el) for el in input().split()]
    print(solve(array))
