class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])

        l, r = 0, width * height - 1

        def index(col: int, row: int) -> int:
            return width * row + col
        def pos(i: int) -> (int, int):
            row = i // width
            col = i % width
            return (col, row)
        
        while l <= r:
            mid = math.floor((l + r) / 2)
            col, row = pos(mid)
            print(row, col)
            el = matrix[row][col]

            if el == target:
                return True
            elif el < target:
                l = mid + 1
            elif el > target:   
                r = mid - 1
        
        return False