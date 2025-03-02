def correct(a, b):
    """Returns True iff a << b.
    """
    ldigit_a = a % 10
    ldigit_b = b % 10
    if ldigit_a > ldigit_b:
        return False
    if ldigit_a == ldigit_b and a > b:
        return False
    else:
        return True

def solve(lst):
    n = len(lst)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if correct(lst[i], lst[i+1]):
                pass
            else:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

if __name__ == "__main__":
    am = int(input())
    lst = []
    for i in range(am):
        lst.append(int(input()))
    solve(lst)
    print(" ".join(map(str, lst)))