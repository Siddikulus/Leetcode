'''
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.



Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.


Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
'''

from DSinitialization.data_structure_initialization import Linkedlist
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        count = len(arr)
        parts = count//k
        extras = count%k
        result = []
        temp = head
        for i in range(k):
            result.append(temp)
            current_part_size = parts + 1 if extras > 0 else parts
            extras -= 1
            for j in range(current_part_size - 1):
                temp = temp.next
            if temp:
                temp.next, temp = None, temp.next

        return result


listhead1 = Linkedlist().append([1])

head = Solution().splitListToParts(listhead1, 11)
print(head)
# while head:
#     print(head.val)
#     head = head.next