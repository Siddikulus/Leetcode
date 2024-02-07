'''
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.



Example 1:


Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.


Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
'''

from DSinitialization.data_structure_initialization import Linkedlist
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        curr = list1
        count = 1
        while count < a:
            count += 1
            curr = curr.next
        last = curr
        while count <= b:
            count+=1
            last = last.next
        curr.next = list2
        while curr.next != None:
            curr = curr.next
        curr.next = last.next
        return list1



listhead1 = Linkedlist().append([0,1,2,3,4,5,6])
listhead2 = Linkedlist().append([1000000,1000001,1000002,1000003,1000004])

head = Solution().mergeInBetween(listhead1, 2, 5, listhead2)

while head:
    print(head.val)
    head = head.next