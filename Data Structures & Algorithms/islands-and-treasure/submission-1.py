from collections import deque

INF = 2147483647
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque() # (col, row, path_size)

        for row_i, row in enumerate(grid):
            for col_i, cell in enumerate(row):
                if cell == 0:
                    for (dx, dy) in directions:
                        q.append((col_i + dx, row_i + dy, 1))
                
        while q:
            col, row, dis = q.popleft()

            if col < 0 or col >= len(grid[0]):
                continue
            if row < 0 or row >= len(grid):
                continue
            
            if grid[row][col] == -1 or grid[row][col] != 2147483647:
                continue

            grid[row][col] = dis

            for dx, dy in directions:
                q.append((col + dx, row + dy, dis + 1))

            
        

            


