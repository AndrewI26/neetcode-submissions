class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = float("-inf")
        largest_i = -1
        for iteration in range(k):
            for i, num in enumerate(nums):
                if num == largest:
                    largest_i = i
                if num > largest:
                    largest = num
                    largest_i = i
            nums[largest_i] = float("-inf")
            if iteration < k - 1:
                largest = float("-inf")
                largest_i = []
                

        print(largest, largest_i, nums)
        return largest