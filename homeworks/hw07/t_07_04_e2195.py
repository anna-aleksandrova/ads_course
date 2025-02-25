import math
EMPTY = None

def is_prime(n):
    for i in range(2, math.sqrt(n) + 1):
        if n % i == 0:
            return False
        else:
            return True
        
class Set:
    M = 1000003

    def __init__(self, size = M):
        self._size = size
        self._keys = [EMPTY for _ in range(self._size)]
        self._count = 0

    def hash(self, key):
        return key % self._size
    
    def rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2
        
        keys = self._keys
        self.__init__(self._size)
        for key in keys:
            self.add(key)
    
    def add(self, key):
        if 0.7 * self._size < self._count:
            self.rehash()
        current = self.hash(key)
        while self._keys[current] is not EMPTY:
            if self._keys[current] == key:
                return
            current = (current + 1) % self._size
        self._keys[current] = key
        self._count += 1
    
    def __contains__(self, key):
        current = self.hash(key)
        while self._keys[current] is not EMPTY:
            if self._keys[current] == key:
                return True
        return False
    
    def difference(self, other):
        res = Set()
        for el in self._keys:
            if not (el in other):
                res.add(el)
        return res

    def __len__(self):
        return self._count

def solve(needed: set, used: set):
    if len(used.difference(needed)) != 0:
        print("Some words from the text are unknown.")
    elif len(needed.difference(used)) != 0:
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")

if __name__ == "__main__":
    N, M = map(int, input().split())
    needed = set()
    for i in range(N):
        needed.add(input())
    used = set()
    for i in range(M):
        line = str(input())
        word = ""
        for el in line:
            if el.isalpha():
                word += el.lower()
            else:
                if word:
                    used.add(word)
                word = ""
        if word:
            used.add(word)
    solve(needed, used)