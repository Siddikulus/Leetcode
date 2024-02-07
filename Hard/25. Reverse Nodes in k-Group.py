'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000


Follow-up: Can you solve the problem in O(1) extra memory space?
'''

from DSinitialization.data_structure_initialization import Linkedlist
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # count = 0
        # curr = head
        # prev = head
        # link = head
        # dummy = None
        # while curr:
        #     count+=1
        #     if count <= k:
        #         curr = curr.next
        #     if count > k:
        #         while prev != curr:
        #             nextnode = prev.next
        #             prev.next = dummy
        #             dummy = prev
        #             prev = nextnode
        #         link.next = curr
        #         link = link.next
        #         count = 0
        #         dummy = None
        # return head

#Couldn't solve


listhead1 = Linkedlist().append([1,2,3,4,5])

head = Solution().reverseKGroup(listhead1, k = 2)

while head:
    print(head.val)
    head = head.next