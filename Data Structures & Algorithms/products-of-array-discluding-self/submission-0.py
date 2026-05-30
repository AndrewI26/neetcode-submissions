class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for num in nums[1::]:
           prefix.append(prefix[-1]*num) 

        postfix = [nums[-1]]
        reverse = nums[::-1]
        for num in reverse[1::]:
            postfix.append(postfix[-1]*num)
        
        postfix = postfix[::-1]


        res = []
        for i in range(len(nums)):
            print(i)
            if i == 0:
                res.append(postfix[i+1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*postfix[i+1])
        
        return res