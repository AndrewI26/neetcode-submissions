'''
stack = []  
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (i, temp) sorted desc temp
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                lower_temp = stack.pop()
                res[lower_temp[0]] = i - lower_temp[0]

            stack.append((i, temp))
        
        return res