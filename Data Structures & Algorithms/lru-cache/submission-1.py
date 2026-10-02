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
        if key in self.cache:
            self.cache[key] = value

            self.used_q.remove(key)
            self.used_q.append(key)
        else:
            if len(self.used_q) == self.capacity:
                rem = self.used_q.popleft()
                del self.cache[rem]

            self.cache[key] = value
            self.used_q.append(key)
        
