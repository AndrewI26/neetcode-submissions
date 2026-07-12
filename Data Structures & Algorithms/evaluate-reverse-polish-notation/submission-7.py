class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num = stack.pop()
                stack[-1] += num
            elif token == "-":
                num = stack.pop()
                stack[-1] -= num
            elif token == "*":
                num = stack.pop()
                stack[-1] *= num
            elif token == "/":
                num = stack.pop()
                stack[-1] = int(stack[-1] / num)
            else:
                stack.append(int(token))

        return stack[0]