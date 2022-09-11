# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            currnext = curr.next
            curr.next = prev
            prev = curr
            curr = currnext
        return prev
'''
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head               
        nxt = head.next               
        prv = None                    
        while nxt:
            tmp = head               
            head = nxt                
            nxt = head.next           
            head.next = tmp           
            head.next.next = prv      
            prv = tmp                 
        return head
'''
#recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = [None]
        def reverse(node, prev=None):
            #print(node)
            #print(prev)
            if node is None:
                last[0] = prev
                return
            reverse(node.next, node)
            node.next = prev
        reverse(head)
        return last[0]


