# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if root:

            res.append(root.val)
            if root.left is not None:
                res.extend(self.preorderTraversal(root.left))
            if root.right is not None:
                res.extend(self.preorderTraversal(root.right))

        return res



# 2nd solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)