from collections import deque

INF = 2147483647
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque() # (col, row, path_size)

        for row_i, row in enumerate(grid):
            for col_i, cell in enumerate(row):
                if cell == 0:
                    for (dx, dy) in directions:
                        queue.append((col_i + dx, row_i + dy, 0))
                
        for chest in queue:
            q = deque([chest])
            seen = set()

            while q:
                col, row, path_size = q.popleft()

                if (col, row) in seen:
                    continue
                if col < 0 or col >= len(grid[0]):
                    continue
                if row < 0 or row >= len(grid):
                    continue
                if grid[row][col] == -1 or grid[row][col] == 0:
                    continue
                
                grid[row][col] = min(grid[row][col], path_size + 1)

                for (dx, dy) in directions:
                    q.append((col + dx, row + dy, path_size + 1))
                
                seen.add((col, row)) 

            


