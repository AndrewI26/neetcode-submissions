class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            "]": "[",
            "}": "{",
            ")": "(",
        }

        for bracket in s:
            if bracket in ["[", "{", "("]:
                stack.append(bracket)
            else:
                if len(stack) == 0 or close_to_open[bracket] != stack.pop():
                    return False

        return len(stack) == 0

                