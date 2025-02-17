def breal_search(f, c, a, b):
    """
    Args:
        f (function): Non-decreasing continious function on [a, b].
        c (float): f(x) = c.
        a, b (float): Endpoints of [a, b].
    
    Returns:
        x (float): The approximate solution of the equation f(x) = c.
    """
    left = a
    right = b
    m = (left + right) / 2.0
    while left != m and right != m:
        if f(m) > c:
            right = m
        else:
            left = m
        return m

if __name__ == "__main__":
    print(breal_search(lambda x: x ** 3 + 4 * x ** 2 + x - 6, 0, 0, 2))  # result: 1.0
