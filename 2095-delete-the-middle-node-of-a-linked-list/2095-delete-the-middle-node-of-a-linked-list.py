# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        slow.next = slow.next.next
        return dummy.next
        '''
        '''
        aux = []
        
        while head:
            curr = head
            aux.append(head.val)
            head = head.next
            
        middle = int(len(aux)/2)
        aux = aux[:middle:] + aux[middle+1::]
        
        head = ListNode()
        tail = head
        
        for i in aux:
            curr = ListNode(i)
            tail.next = curr
            tail = curr
            
        return head.next
        '''
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #BASE case
        if head.next == None:
            return None
        elif head.next.next == None:
            head.next = None
            return head
        
        #slow and fast pointer
        else:
            slow = head
            fast = head.next.next
        
            while(fast != None):
                fast = fast.next
                if fast == None:
                    slow.next = slow.next.next
                    return head
                fast = fast.next
                slow = slow.next
        
            slow.next = slow.next.next
            return head