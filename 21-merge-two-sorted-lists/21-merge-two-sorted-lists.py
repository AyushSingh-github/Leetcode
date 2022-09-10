# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = prev = ListNode()
        get = lambda x,y: x if x.val < y.val else y
        while l1 and l2:
            prev.next = prev = (mini := get(l1,l2))
            if mini == l1: l1 = l1.next
            else: l2 = l2.next
        prev.next = l1 or l2
        return head.next