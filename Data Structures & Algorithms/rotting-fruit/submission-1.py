from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for row_i in range(len(grid)):
            for col_i in range(len(grid[0])):
                if grid[row_i][col_i] == 2:
                    q.append((col_i, row_i))
        
        second = 0
        while True:
            search_len = len(q)
            if search_len == 0:
                break

            for _ in range(search_len):
                (col, row) = q.popleft()

                for (dx, dy) in directions:
                    new_x = dx + col
                    new_y = dy + row

                    if not 0 <= new_y < len(grid) or not 0 <= new_x < len(grid[0]): continue

                    if grid[new_y][new_x] == 1:
                        q.append((new_x, new_y))
                        grid[new_y][new_x] = 2

            second += 1
        
        for row in grid:
            for el in row:
                if el == 1: return -1
        
        return max(0, second - 1)


            


