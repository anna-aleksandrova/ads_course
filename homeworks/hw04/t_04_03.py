def breal_search(f, c, a, b):
    """
    Args:
        f (function): Non-decreasing continious function on [a, b].
        c (float): f(x) > c.
        a, b (float): Endpoints of [a, b].
    
    Returns:
        x (float): The least x such that f(x) > c.
    """
    left = a
    right = b
    m = (left + right) / 2.0
    while left != m and right != m:
        if f(m) <= c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0
    return m

if __name__ == "__main__":
    print(breal_search(lambda x: x ** 3 + x + 1, 5, 0, 10))  # result: 1.3787967001295511
