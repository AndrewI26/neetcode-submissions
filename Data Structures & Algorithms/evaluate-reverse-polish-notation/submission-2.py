class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                sum_stack = sum(stack)
                stack = [sum_stack]
            elif token == "-":
                diff = stack[0]
                for num in stack[1:]:
                    diff -= num
                stack = [diff]
            elif token == "*":
                prod = stack[0]
                for num in stack[1:]:
                    prod *= num
                stack = [prod]
            elif token == "/":
                quo = stack[0]
                for num in stack[1:]:
                    quo = quo // num
                stack = [quo]
               
            else:
                stack.append(int(token))

        return stack[0]