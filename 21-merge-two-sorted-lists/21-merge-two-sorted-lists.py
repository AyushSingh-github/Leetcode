# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        head = prev = ListNode()
        get = lambda x,y: x if x.val < y.val else y
        while l1 and l2:
            prev.next = prev = (mini := get(l1,l2))
            if mini == l1: l1 = l1.next
            else: l2 = l2.next
        prev.next = l1 or l2
        return head.next
        '''    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode])-> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        while list2 is not None:
            nodeA, nodeB = list1, list2
            list2 = list2.next

            if nodeB.val <= nodeA.val:
                nodeB.next = nodeA
                list1 = nodeB
            else:
                prev = None
                while nodeA is not None and nodeB.val > nodeA.val:
                    prev = nodeA
                    nodeA = nodeA.next

                temp = prev.next
                prev.next = nodeB
                nodeB.next = temp

        return list1