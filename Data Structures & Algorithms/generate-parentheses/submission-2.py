class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(opened: int, closed: int, path: list[str]):
            if len(path) == n * 2:
                res.append("".join(path))
            
            if opened < n:
                path.append("(")
                backtrack(opened + 1, closed, path)
                path.pop()
            
            if closed < opened:
                path.append(")")
                backtrack(opened, closed + 1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return res
        