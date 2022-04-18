# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        nodes = []
        self.solve(root, nodes)
        return nodes[k-1]
        
    def solve(self, root, nodes):
        if root is None:
            return None
            
        self.solve(root.left, nodes)
        nodes.append(root.val)
        self.solve(root.right, nodes)
            
        
        
    
