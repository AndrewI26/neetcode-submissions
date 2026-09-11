'''
res = []
cache = 2d arr r x c

for r in range():
    for l in range()

[[1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]
 ]
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        cache = {} # { (r, c): (reaches_atlantic: bool, reaches_pacfici: bool) }

        for c in range(len(heights[0])):
            for r in range(len(heights)):
                def dfs(r, c) -> (bool, bool):
                    reaches_atlantic = False
                    reaches_pacific = False

                    if (r, c) in cache:
                        return cache[(r, c)]
                    
                    if 0 <= r < len(heights) and 0 <= c < len(heights[0]) and heights[r][c] == -1:
                        return (False, False)

                    # up check
                    if r < 0: 
                        cache[(r, c)] = (False, True)
                        return (False, True)
                    # down check
                    if r >= len(heights): 
                        cache[(r, c)] = (True, False)
                        return (True, False)
                    # right check
                    if c >= len(heights[0]): 
                        cache[(r, c)] = (True, False)
                        return (True, False)
                    # left check
                    if c < 0: 
                        cache[(r, c)] = (False, True)
                        return (False, True)

                    
                    curr_height = heights[r][c]
                    if 0 <= r < len(heights) and 0 <= c < len(heights[0]):
                        heights[r][c] = -1

                    deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                    for (r_delta, c_delta) in deltas:
                        new_r, new_c = r + r_delta, c + c_delta
                        if 0 <= new_r < len(heights) and 0 <= new_c < len(heights[0]) and not heights[new_r][new_c] <= curr_height:
                            continue
                        
                        (reaches_a, reaches_p) = dfs(new_r, new_c)
                        if reaches_a:
                            reaches_atlantic = True
                        if reaches_p:
                            reaches_pacific = True
                    result = (reaches_atlantic, reaches_pacific)
                    cache[(r, c)] = result

                    if reaches_atlantic and reaches_pacific:
                        res.append([r ,c])
                    return result
                
                dfs(r, c)
        
        return res




