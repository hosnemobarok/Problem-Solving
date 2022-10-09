# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        nums = []
        def preOrder(root):
            if not root:
                return False
            
            else:
                nums.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
                
        preOrder(root)

        nums.sort()

        left = 0
        right = len(nums)-1
        while left < right:
            s = nums[left] + nums[right]

            if s == k:
                return True
            
            elif s > k:
                right -= 1
            else:
                left += 1

        return False
