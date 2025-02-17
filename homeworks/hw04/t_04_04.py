import math

def breal_search(f, c, a, b):
    """
    Args:
        f (function): Non-increasing continious function on [a, b].
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
            left = m
        else:
            right = m
        m = (left + right) / 2.0
    return m

if __name__ == "__main__":
    print(breal_search(lambda x: math.sin(x) - x / 3.0, 0, 1.6, 3.0))  # result: 2.278862660075828
    