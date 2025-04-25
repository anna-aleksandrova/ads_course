from math import log2, gcd

class SegmentTree:
    def __init__(self, array):
        n = (1 << int(log2(len(array)-1))+1)
        self.size = n
        self.items = 2*n*[0]

        for i in range(len(array)):
            self.items[n + i] = array[i]

        for i in range(n-1, 0, -1):
            self.items[i] = gcd(self.items[2*i], self.items[2*i+1])
    
    def update(self, pos, x):
        pos += self.size
        self.items[pos] = x
        i = pos // 2
        while i > 0:
            self.items[i] = gcd(self.items[2*i], self.items[2*i+1])
            i //= 2
    
    def _gcd(self, left, right):
        left += self.size
        right += self.size
        res = 0
        while left <= right:
            if left % 2 == 1:
                res = gcd(res, self.items[left])
            if right % 2 == 0:
                res = gcd(res, self.items[right])
            
            left = (left + 1) // 2
            right = (right - 1) // 2
        return res

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        array = [int(el) for el in f.readline().split()]
        q = int(f.readline())
        st = SegmentTree(array)
        for _ in range(q):
            cmd, *args = f.readline().split()
            if cmd == "1":
                print(st._gcd(int(args[0])-1, int(args[1])-1))
            elif cmd == "2":
                st.update(int(args[0])-1, int(args[1]))
