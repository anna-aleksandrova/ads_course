def qsort(array, a, b):
    if a >= b:
        return

    pivot = array[a + (b - a) // 2]
    left = a
    right = b

    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left >= right:
            break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    
    qsort(array, a, right)
    qsort(array, right + 1, b)

def solve():
    _ = int(input())
    array = [int(el) for el in input().split()]
    qsort(array, 0, len(array) - 1)
    print(" ".join(map(str, array)))

if __name__ == "__main__":
    solve()