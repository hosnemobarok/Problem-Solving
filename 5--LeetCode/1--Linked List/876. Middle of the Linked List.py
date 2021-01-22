# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current_node = head
        arr = []
        while current_node:
            arr.append(current_node)
            current_node = current_node.next

        return arr[len(arr) // 2]