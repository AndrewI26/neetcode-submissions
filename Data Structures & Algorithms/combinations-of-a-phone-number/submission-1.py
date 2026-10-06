''' 3 4
        start
      d       e.      f
g.    h.  i.  g.  h. i.  g h.  i
'''

dig_to_letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        combos = []
        def backtrack(i: int, cur_path: List[str]):
            if i == len(digits) and cur_path:
                combos.append("".join(cur_path))
                return
            
            for letter in dig_to_letters[digits[i]]:
                cur_path.append(letter)
                backtrack(i + 1, cur_path)
                cur_path.pop()
        
        backtrack(0, [])
        return combos

            
