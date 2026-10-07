'''
aa b

aab
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtracking(i: int, cur_path: list[int]):
            if i == len(s):
                res.append(cur_path.copy())
                return

            for j in range(i + 1, len(s) + 1):
                is_palindrome = s[i:j] == s[i:j][::-1]
                print(s[i:j], " | ", s[i:j][::-1])

                if is_palindrome:
                    cur_path.append(s[i:j])
                    backtracking(j, cur_path)
                    cur_path.pop()
            
        backtracking(0, [])
        return res

