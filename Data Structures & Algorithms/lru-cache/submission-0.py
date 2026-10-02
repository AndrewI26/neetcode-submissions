'''
{
    k: v
}

[]

'''
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.used_q = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.used_q.remove(key)    
        self.used_q.append(key)

        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if len(self.used_q) == self.capacity:
            removed = self.used_q.popleft()
            del self.cache[removed]
            
        self.cache[key] = value
        self.used_q.append(key)
        
