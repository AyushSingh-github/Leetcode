# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
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
'''    
'''
    # SC=O(1)
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
'''    
class Solution:
# SC = O(m*n) using dummy node For simplicity, we create a dummy node to which we attach nodes from lists. We iterate over lists using two-pointers and build up a resulting list so that values are monotonically increased.

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#It creates a single ListNode() object and its reference is saved in both variables (cur and dummy). Dummy is used to keep the head of the new list and cur is used for saving the current last element when creating the list during the while statement
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next