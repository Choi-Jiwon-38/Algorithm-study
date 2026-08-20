"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if node is None:
            return None

        copies = {}

        def dfs(n):
            if n in copies:
                return copies[n]
            
            copy = Node(n.val)
            copies[n] = copy

            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)