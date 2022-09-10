# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #recursion
        '''
        def delete(head,val):
            if head==None:
                return head
            head.next = delete(head.next,val)
            
            if head.val==val:
                return head.next
            else:
                return head
        return delete(head,val)
        '''
        
        #iteration
        '''
        result = current = ListNode(0, head)
        #print(current.val)
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else: 
                current = current.next
        #print(ListNode(0,head))
        return result.next
        '''
    
        tmp = head 
        while tmp is not None:
            while tmp.next is not None and tmp.next.val == val:
                tmp.next = tmp.next.next
            tmp = tmp.next
        if head is not None and head.val == val:
            head = head.next
        return head    