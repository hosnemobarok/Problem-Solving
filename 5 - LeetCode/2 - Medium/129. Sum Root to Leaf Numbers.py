# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root):
        return self.sumNumbers_util(root, 0)

    def sumNumbers_util(self, root, val: int) -> int:
        if root is None:
            return 0

        # To keep on generating the number from the encountered values
        val = val * 10 + root.val

        if not root.left and not root.right:
            return val

        l_node = self.sumNumbers_util(root.left, val)
        r_node = self.sumNumbers_util(root.right, val)

        return l_node + r_node