# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        if head is None:
            return

        res = ''

        current = head
        while current:
            res += str(current.val)

            current = current.next

        return int(res, 2)