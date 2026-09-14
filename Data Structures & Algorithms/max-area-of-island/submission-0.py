class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def is_in_bounds(col, row):
            return 0 <= col < len(grid[0]) and 0 <= row < len(grid)
        def mark_island(col, row) -> int:
            if not is_in_bounds(col, row): return 0

            if grid[row][col] == 1:
                grid[row][col] = 0
            else:
                return 0

            deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            total = 1
            for delta_x, delta_y in deltas:
                total += mark_island(col + delta_x, row + delta_y)
            return total

        for row_i, row in enumerate(grid):
            for col_i, el in enumerate(row):
                if el == 1:
                    count = mark_island(col_i, row_i)
                    max_area = max(max_area, count)

        return max_area