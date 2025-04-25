from math import log2, gcd, lcm, ceil

class SegmentTree:
    def __init__(self, array):
        n = 1 << ceil(log2(len(array)))
        self.size = n
        self.items = 2*n*[0]
        self.items2 = 2*n*[1]

        for i in range(len(array)):
            self.items[n + i] = array[i]
            self.items2[n + i] = array[i]

        for i in range(n-1, 0, -1):
            self.items[i] = gcd(self.items[2*i], self.items[2*i+1])
            self.items2[i] = lcm(self.items2[2*i], self.items2[2*i+1])
    
    def update(self, pos, x):
        pos += self.size
        self.items[pos] = x
        self.items2[pos] = x
        i = pos // 2
        while i > 0:
            self.items[i] = gcd(self.items[2*i], self.items[2*i+1])
            self.items2[i] = lcm(self.items2[2*i], self.items2[2*i+1])
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
    
    def _lcm(self, left, right):
        left += self.size
        right += self.size
        res = 1
        while left <= right:
            if left % 2 == 1:
                res = lcm(res, self.items2[left])
            if right % 2 == 0:
                res = lcm(res, self.items2[right])
            
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
            i, j = int(args[0]), int(args[1])
            if cmd == "1":
                v = st._gcd(i-1, j-1)
                s = st._lcm(i-1, j-1)
                if v < s:
                    print("wins")
                elif v > s:
                    print("loser")
                else:
                    print("draw")
            elif cmd == "2":
                st.update(i-1, j)
