# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        l = []
        num1,num2 = "",""
        
        while head1:
            num1 += str(head1.val)
            head1 = head1.next
            
        while head2:
            num2 += str(head2.val)
            head2 = head2.next
            
        sum1 = int(num1[::-1]) + int(num2[::-1])
        
        l = [int(i) for i in str(sum1)]
        
        for index,value in enumerate(l):
            if index==0:
                l[index] = ListNode(val=value,next=None)
            else:
                l[index] = ListNode(val=value,next=l[index-1])
        
        return l[len(l)-1]