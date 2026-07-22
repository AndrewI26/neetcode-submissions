class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            left = numbers[l]
            right = numbers[r]
            if left + right > target:
                r -= 1
                l = 0

        return [l+1, r+1]