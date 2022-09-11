# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iteration
        '''
        if not head:
            return
        temp = head
        while temp.next is not None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
        '''
        
        #recursion
        if head and head.next:
            if head.val == head.next.val:
                return self.deleteDuplicates(head.next)
            head.next = self.deleteDuplicates(head.next)
        return head