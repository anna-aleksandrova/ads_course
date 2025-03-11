N: int # max length of the tape
max_score: int # max length of recording
array: list[int] # contains the length of every track

def max(score: int, num: int):
    global max_score
    if max_score == N:
        return
    
    if score > N:
        return
    if num == len(array):
        if score > max_score:
            max_score = score
        return
    max(score + array[num], num + 1)
    max(score, num + 1)
    

if __name__ == "__main__":
    f = open("input.txt")
    while True:
        current = f.readline()
        if not current:
            break
        arr = [int(x) for x in current.split()]
        N = arr[0]
        array = arr[2:]
        max_score = 0
        max(0, 0)
        print(f"sum:{max_score}")
    f.close()
