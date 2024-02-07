'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

from DSinitialization.data_structure_initialization import Linkedlist
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            second.next = first
            curr.next = second
            curr = curr.next.next
        return dummy.next

listhead1 = Linkedlist().append([1,2,3,4])

head = Solution().swapPairs(listhead1)

while head:
    print(head.val)
    head = head.next
