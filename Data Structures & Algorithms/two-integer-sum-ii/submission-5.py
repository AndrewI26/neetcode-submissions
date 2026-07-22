class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            if l +1 == r:
                r = len(numbers) - 1
                l += 1
    
            r -= 1

        return [l+1, r+1]