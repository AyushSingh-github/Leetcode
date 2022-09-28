# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #TC - O(N)
        #add dummy node to first node and point left to dummy and right to head (left is behind right)
        dummy = ListNode(0,head)
        left = dummy
        right = head
        
        #move right till nth pos ahead of start and some node
        while n>0 and right:
            right = right.next
            n-=1
        
        #if right not null so incr some both left and right
        while right:
            left = left.next
            right = right.next
        
        #left if just behind the nth node from last
        left.next = left.next.next
        
        return dummy.next