class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers_at_freq = [set() for i in range(len(nums))]
        freq_nums = {}

        for num in nums:
            count = freq_nums.get(num, 0) + 1
            freq_nums[num] = count
            numbers_at_freq[count - 1].add(num)

        top_k = set()
        i = len(nums) - 1
        while len(top_k) < k and i >= 0:
            top_k = top_k | numbers_at_freq[i]
            i -= 1
        
        return [el for el in top_k]
            