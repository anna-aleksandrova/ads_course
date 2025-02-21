def __lt__(time1, time2):
    for i in range(3):
        if time1[i] < time2[i]:
            return time1
    return time2

def sort(array):
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
    am = int(input())
    times = []
    for i in range(am):
        time = [int(el) for el in input().split()]
        times.append(time)
    sort(times)
    for time in times:
        print(" ".join(map(str, time)))
        