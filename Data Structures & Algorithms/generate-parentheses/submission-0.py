class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(num_open: int, path: list[str]):
            if len(path) == n * 2:
                res.append("".join(path))
            
            if num_open == 0:
                path.append("(")
                backtrack(1, path)
                path.pop()
                return
            if num_open < 0:
                return
            
            brackets_left = n * 2 - len(path)
            if num_open > brackets_left:
                return
            elif num_open == brackets_left:
                path.append(")")
                backtrack(num_open - 1, path)
                path.pop()
                return
            
            path.append("(")
            backtrack(num_open + 1, path)
            path.pop()

            path.append(")")
            backtrack(num_open - 1, path)
            path.pop()
        
        backtrack(0, [])
        return res
        