"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cache: dict[int, Node] = {}

        def bfs(node):
            if not node: return None
            if node.val in cache: return cache[node.val]


            new_node = Node(node.val) if node.val not in cache else cache[node.val]
            if node.val not in cache: cache[node.val] = new_node

            new_neighbors = [bfs(n) for n in node.neighbors]
            new_node.neighbors = new_neighbors

            return new_node

        new = bfs(node)
        return new