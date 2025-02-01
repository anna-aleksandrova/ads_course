# n = int(input())

def ones(n):
    sum = 0
    while n != 0:
        sum += (n & 1)
        n =  n >> 1
    return sum

if __name__ == "__main__":
    print(ones(5))