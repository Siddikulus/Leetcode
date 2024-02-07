'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
'''

from DSinitialization.data_structure_initialization import Linkedlist

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        lastval = count - n + 1
        dummyhead = ListNode(-1)
        dummyhead.next = head
        dum = dummyhead
        count = 0
        while count < lastval-1:
            count += 1
            dum = dum.next
        if dum.next and dum.next.next:
            dum.next = dum.next.next
        else:
            dum.next = None
        return dummyhead.next

listhead2 = Linkedlist().append([1])

head = Solution().removeNthFromEnd(listhead2, n = 1)

while head:
    print(head.val)
    head = head.next