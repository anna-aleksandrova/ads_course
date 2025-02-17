import math

def lcyclic_shift(n, am):
    """Left cyclic shift of binary representation of <n>.
    1000 -> 0001
    """
    high = n >> (am - 1)
    res = ((n - (high << (am - 1))) << 1) + high
    return res

def max_shifts(n):
    am = int(math.log(n, 2)) + 1
    res = n
    for i in range(am-1):
        n = lcyclic_shift(n, am)
        if n > res:
            res = n
    return res

if __name__ == "__main__":
    n = 10
    print(max_shifts(n))