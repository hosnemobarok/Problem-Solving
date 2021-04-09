# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''


        res = []
        def inorder(root):
            if root is None:
                return []

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
'''


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)