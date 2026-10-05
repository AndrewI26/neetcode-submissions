directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def backtrack(col: int, row: int, i: int):
            if (col, row) in seen:
                return False

            if i >= len(word):
                return True
            if not (0 <= col < len(board[0]) and 0 <= row < len(board)):
                return False
            
            if word[i] != board[row][col]:
                return False
            
            seen.add((col, row))

            for dx, dy in directions:
                res = backtrack(col + dx, row + dy, i + 1)
                if res:
                    return True
                
            return False

        for row_i, row in enumerate(board):
            for col_i, el in enumerate(row):
                if el == word[0]:
                    res = backtrack(col_i, row_i, 0)
                    if res:
                        return True
        return False


        