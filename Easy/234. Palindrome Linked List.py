'''
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
'''

from DSinitialization.data_structure_initialization import Linkedlist
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        curr = head
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans == ans[::-1]

listhead1 = Linkedlist().append([1,2,2,1])
print(Solution().isPalindrome(listhead1))

# while head:
#     print(head.val)
#     head = head.next