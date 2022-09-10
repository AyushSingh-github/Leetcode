# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return head
        if head.next == head : return True
        if not head.next : return False
        
        while head:
            if head.val==float("infinity"):
                return True
            else:
                head.val=float("infinity")
                head=head.next
        return False
        '''
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False        
        '''
        '''
        visited = set()
        while head :
            if head in visited : return True
            visited.add(head)
            head = head.next
        return False
        '''
        '''
        slow = head.next
        fast = head.next.next
        
        if not fast :
            return False if slow else True 
        
        while fast.next and fast.next.next:
            if slow==fast : return True
            slow = slow.next
            fast = fast.next.next
        return False
        '''