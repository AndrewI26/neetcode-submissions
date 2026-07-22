class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # [[], [], ..., []] size of len(nums) 

        freq = [[] for i in range(len(nums))]
        freq_hash = {}

        for num in nums:
            if num in freq_hash:
                freq[freq_hash[num]].remove(num)
                freq_hash[num] += 1
                freq[freq_hash[num]].append(num)
            else:
                freq_hash[num] = 0
                freq[0].append(num)

        res = []
        size = 0
        i = 0
        while True:
            if size == k:
                return res
            index = k - i
            res += freq[index]
            size += len(freq[index])
            i += 1

            

                

