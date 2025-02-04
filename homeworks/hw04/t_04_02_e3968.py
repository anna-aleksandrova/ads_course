import math

def f(x):
    return x * x + math.sqrt(x)
 
def breal_search(f, c, a, b):
    """Approximately solves the equation f(x) = c, a <= x <= b,
    f is a non-decreasing function on [a, b].
    """
    left = a
    right = b
    m = (left + right) / 2.0
    while left != m and right != m:
        if f(m) < c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0
    return left

if __name__ == "__main__":
    a = 0
    b = 10 ** 5
    c = float(input())
    print(breal_search(f, c, a, b))