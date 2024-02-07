'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

from DSinitialization.data_structure_initialization import Linkedlist


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lessthan = ListNode(-1)
        l = lessthan
        greaterthan = ListNode(-2)
        g = greaterthan

        curr = head
        while curr:
            if curr.val < x:
                l.next = curr
                curr = curr.next
                l = l.next
            else:
                g.next = curr
                curr = curr.next
                g = g.next

        l.next = None
        g.next = None
        l.next = greaterthan.next
        return lessthan.next


listhead1 = Linkedlist().append([2,1])

head = Solution().partition(listhead1, x = 2)

while head:
    print(head.val)
    head = head.next