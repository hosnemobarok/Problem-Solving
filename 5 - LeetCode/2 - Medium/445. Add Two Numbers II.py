# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return

        _l1 = ''
        _l2 = ''

        while l1 is not None:
            _l1 += str(l1.val)
            l1 = l1.next

        while l2 is not None:
            _l2 += str(l2.val)
            l2 = l2.next

        addlist = str(int(_l1) + int(_l2))

        head = ListNode(int(addlist[0]))
        temp = head

        for i in range(1, len(addlist)):
            head.next = ListNode(int(addlist[i]))

            head = head.next

        return temp

