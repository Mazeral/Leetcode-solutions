# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        visited1 = self.traverse(root1)
        visited2 = self.traverse(root2)
        return visited1 == visited2      
    
    def traverse(self, node, visited=None):
        if visited is None:
            visited = []
        if node.left is None and node.right is None:
            visited.append(node.val)
        if node.left is not None:
            self.traverse(node.left, visited)
        if node.right is not None:
            self.traverse(node.right, visited)
        return visited
