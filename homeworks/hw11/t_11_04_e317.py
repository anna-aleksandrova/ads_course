def karatsuba(A: str, B: str) -> int:
    if int(A) < 10 and int(B) < 10:
        return int(A) * int(B)

    a = len(A)
    b = len(B)
    df = a - b
    if df > 0:
        B = ('0' * df) + B
    elif df < 0:
        A = ('0' * (-df)) + A
    else:
        pass
    if len(A) % 2 == 1:
        A = "0" + A
        B = "0" + B
    m = len(A)
    m2 = m // 2
    high1 = A[:m2]
    low1 = A[m2:]
    high2 = B[:m2]
    low2 = B[m2:]

    z2 = str(karatsuba(high1, high2))
    z0 = str(karatsuba(low1, low2))
    z1 = karatsuba(str(int(high1) + int(low1)), str(int(high2) + int(low2)))

    res = int(z2) * (10 ** (2 * m2)) + (z1 - int(z2) - int(z0)) * (10 ** m2) + int(z0)
    return res


if __name__ == "__main__":
    A, B = input().split()
    print(karatsuba(A, B))