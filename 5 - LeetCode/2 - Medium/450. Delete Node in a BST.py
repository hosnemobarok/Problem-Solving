# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # A function min key value found in that tree
    def minValueNode(self, root):
        if root and root.left:
            return self.minValueNode(root.left)

        return root

    def deleteNode(self, root, key):
        # Base case
        if root is None:
            return root

        # if the key to be deleted is smaller than the root's
        # key then it lies in left subtree
        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        # if the key to be delete is greater then the root's key
        # then it lies in right subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:

            # Node with only child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children Get teh inorder successor
            # smallest in the right subtree
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.val = temp.val

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)

        return root