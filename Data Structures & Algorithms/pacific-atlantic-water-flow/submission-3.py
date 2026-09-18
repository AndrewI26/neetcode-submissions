from collections import deque

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        width = len(heights[0])
        height = len(heights)

        # heights = (isPacfiic, isAtlantic)
        reaches = [[[False, False] for _ in range(width)] for _ in range(height)]

        q = deque() # (col, row, isPacific)

        for col_index in range(width):
            q.append((col_index, 0, True))
            reaches[0][col_index][0] = True

            q.append((col_index, height - 1, False))
            reaches[height - 1][col_index][1] = True
        
        for row_index in range(height):
            q.append((0, row_index, True))
            reaches[row_index][0][0] = True

            q.append((width - 1, row_index, False))
            reaches[row_index][width - 1][1] = True

        while q:
            (col, row, is_pacific) = q.popleft()

            # if reaches[row][col][0 if is_pacific else 1]:
            #     continue
            
            # reaches[row][col][0 if is_pacific else 1] = True

            for dx, dy in directions:
                new_col = col + dx
                new_row = row + dy

                if new_col < 0 or new_col >= width:
                    continue
                if new_row < 0 or new_row >= height:
                    continue 
                
                if reaches[new_row][new_col][0 if is_pacific else 1]:
                    continue
                
                if heights[new_row][new_col] >= heights[row][col]:
                    reaches[new_row][new_col][0 if is_pacific else 1] = True
                    q.append((new_col, new_row, is_pacific))

        res = []
        for row in range(height):
            for col in range(width):
                if reaches[row][col] == [True, True]: 
                    res.append([row, col])

        return res
            



