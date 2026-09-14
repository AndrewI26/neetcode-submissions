'''
2 4 5 8
|     |

l = 0
r = 3

is_closer(2, 8) = false
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        def is_closer(a: int, b: int) -> bool:
            return (abs(a - x) < abs(b - x)) or (a < b and (abs(a - x) == abs(b - x)))

        while r - l + 1 > k:
            if is_closer(arr[l], arr[r]):
                r -= 1
            else:
                l += 1

        return arr[l:r + 1]