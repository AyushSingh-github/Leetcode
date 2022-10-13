# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #TC -> O(N)  , SC -> O(1)
        # Replacing value of each node with the value of the next node
        '''
        temp = node
        while temp.next:
            temp.val = temp.next.val
            temp = temp.next

        # Removing last node
        temp = node
        while temp.next.next:
            temp = temp.next
        temp.next = temp.next.next   
        '''
        
        #TC -> O(N) , shifting the next node val to prev node, without deletion
        node.val = node.next.val
        node.next = node.next.next
        