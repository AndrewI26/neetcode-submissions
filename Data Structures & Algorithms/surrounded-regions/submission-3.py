from collections import deque

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        width = len(board[0])
        height = len(board)

        connected_to_edge = set() #(col, row)

        q = deque()
        for row in range(height):
            q.append((0, row))
            connected_to_edge.add((0, row))

            q.append((width - 1, row))
            connected_to_edge.add((width - 1, row))
        
        for col in range(width):
            q.append((col, 0))
            connected_to_edge.add((col, 0))

            q.append((col, height - 1))
            connected_to_edge.add((col, height - 1))

        while q:
            (col, row) = q.popleft()

            if (col, row) in connected_to_edge:
                continue
            if col < 0 or col >= width:
                continue
            if row < 0 or row >= height:
                continue
            
            for dx, dy in directions:
                new_col = col + dx
                new_row = row + dy

                q.append((new_col, new_row))
                connected_to_edge.add((new_col, new_row))

        
        for row in range(height):
            for col in range(width):
                if board[row][col] == "O" and (row, col) not in connected_to_edge:
                    board[row][col] = "X"


            
            

            

