'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


Follow up: Could you solve it without reversing the input lists?
'''

from DSinitialization.data_structure_initialization import Linkedlist

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        s1 = ''
        while c1:
            s1 += str(c1.val)
            c1 = c1.next

        c2 = l2
        s2 = ''
        while c2:
            s2 += str(c2.val)
            c2 = c2.next

        dummy = ListNode(-1)
        dum = dummy
        totalsum = str(int(s1) + int(s2))
        # print(totalsum)
        for ele in totalsum:
            newnode = ListNode(int(ele))
            dum.next = newnode
            dum = dum.next
        return dummy.next


listhead1 = Linkedlist().append([2,4,3])
listhead2 = Linkedlist().append([5,6,4])

head = Solution().addTwoNumbers(listhead1, listhead2)

while head:
    print(head.val)
    head = head.next