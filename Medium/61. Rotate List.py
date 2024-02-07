'''
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''
from DSinitialization.data_structure_initialization import Linkedlist


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        # base case
        if not head or k == 0:
            return head

        # length of the linked list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        # special k
        if k == length:
            return head
        k = k % length
        if k == 0:
            return head

        # the number of times to move forward
        go = length - k
        first = head
        for i in range(go - 1):
            first = first.next
        nextFirst = first.next
        first.next = None
        if length == 1:
            return head

        # connect two parts
        tail = nextFirst
        while tail.next:
            tail = tail.next
        tail.next = head
        return nextFirst

listhead2 = Linkedlist().append([])

head = Solution().rotateRight(listhead2, k = 2)

while head:
    print(head.val)
    head = head.next