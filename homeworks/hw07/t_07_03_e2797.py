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
        if 0.7 * self._size < self._count:
            self.rehash()

        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2
        
        keys = self._keys
        self.__init__(self._size)
        for key in keys:
            self.add(key)
    
    def add(self, key):
        current = self.hash(key)
        while self._keys[current] is not EMPTY:
            if self._keys[current] == key:
                return
            current = (current + 1) % self._size
        self._keys[current] = key
        self._count += 1

    def __len__(self):
        return self._count

def solve(contacts: list):
    c = Set()
    for contact in contacts:
        c.add(contact)
    return len(c)

if __name__ == "__main__":
    temp = int(input())
    contacts = [int(el) for el in input().split()]
    print(solve(contacts))