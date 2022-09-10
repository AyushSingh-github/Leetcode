# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def delete(head,val):
            if head==None:
                return head
            head.next = delete(head.next,val)
            
            if head.val==val:
                return head.next
            else:
                return head
        return delete(head,val)