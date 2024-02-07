'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
'''

from DSinitialization.data_structure_initialization import Linkedlist
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        dummy = ListNode(-1)
        dummy.next = head
        l,r = dummy,dummy
        lcount, rcount = 0, 0
        while lcount < left-1:
            lcount += 1
            l = l.next
            # print(l.val)
        while rcount < right:
            rcount += 1
            r = r.next
            # print(r.val)
        taillist = r.next
        r.next = None
        reverseptr = l.next
        l.next = None
        prev = None

        while reverseptr:
            nextnode = reverseptr.next
            reverseptr.next = prev
            prev = reverseptr
            reverseptr = nextnode

        curr = dummy
        while curr.next:
            curr = curr.next
        curr.next = prev
        while curr.next:
            curr = curr.next
        curr.next = taillist
        return dummy.next


listhead1 = Linkedlist().append([5])

head = Solution().reverseBetween(listhead1, left = 1, right = 1)

while head:
    print(head.val)
    head = head.next