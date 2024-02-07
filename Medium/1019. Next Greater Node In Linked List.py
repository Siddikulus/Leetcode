'''
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.



Example 1:


Input: head = [2,1,5]
Output: [5,5,0]
Example 2:


Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]


Constraints:

The number of nodes in the list is n.
1 <= n <= 104
1 <= Node.val <= 109

'''

from DSinitialization.data_structure_initialization import Linkedlist
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        curr = head
        vals = []
        while curr:
            vals.append(curr.val)
            curr= curr.next
        ans = [0] * len(vals)
        stack = []

        for i in range(len(vals)):
            while stack and vals[i] > vals[stack[-1]]:
                poppedindex = stack.pop()
                ans[poppedindex] = vals[i]
            stack.append(i)
        return ans

#Full referenced
listhead1 = Linkedlist().append([2,7,4,3,5])

head = Solution().nextLargerNodes(listhead1)
print(head)
# while head:
#     print(head.val)
#     head = head.next