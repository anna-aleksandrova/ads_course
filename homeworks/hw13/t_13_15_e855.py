def correct(sequence: str):
    stack = []
    for el in sequence:
        if el == ")":
            t = stack.pop()
            if t != "(":
                return False
        elif el == "]":
            t = stack.pop()
            if t != "[":
                return False
        else:
            stack.append(el)
    return True

def gen(size: int, sequence: str, check1: int, check2: int, n: int):
    if check1 < 0 or check2 < 0 or sequence[-2:] == "[)" or sequence[-2:] == "(]":
        return
    if size == n:
        if check1 != 0 or check2 != 0:
            return
        if correct(sequence):
            print(sequence)
        return
    else:
        gen(size + 1, sequence + ")", check1 - 1, check2, n)
        gen(size + 1, sequence + "]", check1, check2 - 1, n)
        gen(size + 1, sequence + "(", check1 + 1, check2, n)
        gen(size + 1, sequence + "[", check1, check2 + 1, n)


if __name__ == "__main__":
    n = int(input())
    gen(0, "", 0, 0, n)