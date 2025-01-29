# ----------a----------
def a(n):
    sum = 0                 # O(1)
    for i in range(n+1):    # O(n)
        sum += i            # O(n)
    return sum              # O(1)
# result: O(n)

# ----------b----------
def b(n):
    sum = 0                 # O(1)
    for i in range(n+1):    # O(n)
        sum += i * i        # O(n)
    return sum              # O(1)
# result: O(n)

# ----------c----------
def c(a, n):
    sum = 0                 # O(1)
    p = 1                   # O(1)
    for i in range(n+1):    # O(n)
        sum += p            # O(n)
        p *= a              # O(n)
    return sum              # O(1)
# result: O(n)

# ----------d----------
def d(n):
    sum = 0                  # O(1)
    for i in range(1, n+1):  # O(n)
        sum += i ** i        # C*n + log_1 + ... + log_n <= C*n + n*log_n = O(n*log_n)
    return sum               # O(1)
# result: O(n*log_n) => | n*log_n << n^2 | => O(n^2)

# ----------e----------
def e(n):
    product = 1              # O(1)
    for i in range(1, n+1):  # O(n)
        product /= (1+i)     # O(n)
    return product           # O(1)
# result: O(n)

# ----------f----------
def f(n):
    product = 1               # O(1)
    p = 1                     # O(1)
    i = 1                     # O(1)
    while i <= n:             # O(n)
        product /= (1+p)      # O(n)
        i += 1                # O(n)
        p *= i                # O(n)
    return product            # O(1)
# result: O(n)

# ----------g----------
def g(a, n):
    product = 1               # O(1)
    p = 1                     # O(1)
    i = 1                     # O(1)
    while i <= n:             # O(n)
        product *= a / (1+p)  # O(n)
        i += 1                # O(n)
        p *= i                # O(n)
        a *= a                # O(n)
    return product            # O(1)
# result: O(n)

# ----------h----------
def h(m, n):
    product = 1                  # O(1)
    i = 1                        # O(1)
    while i <= n:                # O(n)
        product /= (1 + i ** m)  # O(C*n + n * log_m) = O(n*log_m)
        i += 1                   # O(n)
    return product               # O(1)
# result: O(n * log_m) => |log_m = O(m)| = O(n*m)

# ----------i----------
def i(n):
    product = 1                  # O(1)
    i = 1                        # O(1)
    while i <= n:                # O(n)
        product /= (1 + i ** i)  # C*n + log_1 + ... + log_n <= C*n  + n*log_n = O(n*log_n)
        i += 1                   # O(n)
    return product               # O(1)
# result: O(n*log_n) => |log_n = O(n)| => O(n^2)
