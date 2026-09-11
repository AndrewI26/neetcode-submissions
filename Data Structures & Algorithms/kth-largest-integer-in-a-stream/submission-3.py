class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.k_largest = nums[:k]

    def add(self, val: int) -> int:
        if self.k_largest and val > self.k_largest[-1]:
            self.k_largest.pop()
            i = 0
            while self.k_largest[i] > val:
                i += 1
            if i < len(self.k_largest):
                self.k_largest.insert(i, val)
            else:
                self.k_largest.append(val)
        else:
            self.k_largest.append(val)
            return val

        
        return self.k_largest[-1]
        
