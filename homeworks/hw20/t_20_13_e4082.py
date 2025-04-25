from math import log2, gcd

class SegmentTree:
    def __init__(self, array):
        n = (1 << int(log2(len(array)-1))+1)
        self.size = n
        self.items = 2*n*[1]

        for i in range(len(array)):
            self.items[n + i] = array[i]

        for i in range(n-1, 0, -1):
            self.items[i] = self.items[2*i] * self.items[2*i+1]
    
    def update(self, pos, x):
        pos += self.size
        self.items[pos] = x
        i = pos // 2
        while i > 0:
            self.items[i] = self.items[2*i] * self.items[2*i+1]
            i //= 2
    
    def prod(self, left, right):
        left += self.size
        right += self.size
        res = 1
        while left <= right:
            if left % 2 == 1:
                res *= self.items[left]
            if right % 2 == 0:
                res *= self.items[right]
            
            left = (left + 1) // 2
            right = (right - 1) // 2
        return res

if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline()
        while line:
            n, k = map(int, line.split())
            array = [int(el) for el in f.readline().split()]
            st = SegmentTree(array)
            for _ in range(k):
                cmd, *args = f.readline().split()
                if cmd == "P":
                    res = st.prod(int(args[0])-1, int(args[1])-1)
                    if res == 0:
                        print("0", end = "")
                    elif res > 0:
                        print("+", end = "")
                    else:
                        print("-", end = "")
                elif cmd == "C":
                    st.update(int(args[0])-1, int(args[1]))
            print()
            line = f.readline()
 