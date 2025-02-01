def contains(array, x):
    """Binary search to check whether <x> is in <array>.
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        elif array[m] > x:
            right = m - 1
        else:
            return True
    return False

if __name__ == "__main__":
    f = open("input.txt")
    while True:
        if not(f.readline()): 
            break
        arr = [int(x) for x in f.readline().split()]
        f.readline()
        needed = [int(x) for x in f.readline().split()]
    f.close()
    for el in needed:
        if contains(arr, el):
            print("YES")
        else:
            print("NO")
    