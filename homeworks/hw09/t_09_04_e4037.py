def merge_sort(array):
    if len(array) <= 1:
        return
    
    mid = len(array) // 2
    lefthalf = array[:mid]
    righthalf = array[mid:]
    merge_sort(lefthalf)     # sorting
    merge_sort(righthalf)

    i = j = k = 0            # merging
    while i < len(lefthalf) and j < len(righthalf):
        if int(lefthalf[i][0]) <= int(righthalf[j][0]):
            array[k] = lefthalf[i]
            i += 1
        else:
            array[k] = righthalf[j]
            j += 1
        k += 1
    
    while i < len(lefthalf):
        array[k] = lefthalf[i]
        i += 1
        k += 1
    while j < len(righthalf):
        array[k] = righthalf[j]
        j += 1
        k += 1

def solve():
    am = int(input())
    robots = []
    for i in range(am):
        robots.append([int(el) for el in input().split()])
    merge_sort(robots)
    for i in range(am):
        print(" ".join(map(str, robots[i])))

if __name__ == "__main__":
    solve()
    