def amount(arr, a, b):
    sum = 0
    for el in arr:
        if a <= el <= b:
            sum += 1
    return sum

if __name__ == "__main__":
    f = open("input.txt")
    while f.readline():
        arr = [int(x) for x in f.readline().split()]
        a, b = [int(x) for x in f.readline().split()]
        print(amount(arr, a, b))
    f.close()
