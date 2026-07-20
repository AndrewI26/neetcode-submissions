class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [i, temp]
        res = [0 for i in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                colder = stack.pop()
                res[colder[0]] = i - colder[0]
            stack.append([i, temp])

        return res