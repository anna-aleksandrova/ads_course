def solve(array):
    size = len(array)
    for i in range(size // 2 + 1):
        if 2*i+1 < size:
            if array[2*i+1] < array[i]:
                return "NO"
        if 2*i + 2 < size:
            if array[2*i+2] < array[i]:
                return "NO"
    return "YES"

if __name__ == "__main__":
    n = int(input())
    array = [int(el) for el in input().split()]
    print(solve(array))