def sequence(lst, n):
    global k
    if len(lst) == k:
        print(*lst)
        return
    for i in range(1, n+1):
        if i not in lst:
            lst_next = lst[:]
            lst_next.append(i)
            sequence(lst_next, n)

if __name__ == "__main__":
    lst = []
    arr = [int(el) for el in input().split()]
    n = arr[0]
    k = arr[1]
    sequence(lst, n)