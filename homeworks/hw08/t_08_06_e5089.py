def solve(array):
    """Sorting a dictionary using insertion sort.
    """
    n = len(array)
    for pos in range(1, n):
        x = array[pos]
        while pos > 0:
            if array[pos - 1] < x:
                break
            else:
                array[pos] = array[pos - 1]
            pos -= 1
        array[pos] = x

if __name__ == "__main__":
    amount = int(input())
    words = []
    for i in range(amount):
        word = input()
        words.append(word)
    solve(words)
    for word in words:
        print(word)