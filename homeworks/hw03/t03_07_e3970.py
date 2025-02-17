def bsearch_leftmost(array, x):
    """Binary search algorithm to find the leftmost
    occurence of <x> in <array>.
    """
    left = 0
    right = len(array)
    while left < right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        else:
            right = m
    if 0 <= left < len(array) and array[left] == x:
        return left
    else:
        return None

def bsearch_rightmost(array, x):
    """Binary search algorithm to find the rightmost
    occurence of <x> in <array>.
    """
    left = 0
    right = len(array) - 1
    while left < right:
        m = left + (right + 1 - left) // 2
        if array[m] > x:
            right = m - 1
        else:
            left = m
    if 0 <= left < len(array) and array[left] == x:
        return left
    else :
        return None

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
        left = bsearch_leftmost(arr, el)
        if left is None:
            print(0)
            continue
        else:
            right = bsearch_rightmost(arr, el)
            print(right - left + 1)
            