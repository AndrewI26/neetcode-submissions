class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set() # set<(r, c)>
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def dfs(r, c):
            if (r, c) in visited:
                return
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            visited.add((r, c))

            for [dx, dy] in directions:
                dfs(r + dx, c + dy)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    res += 1
                    dfs(row, col)
        return res

            
