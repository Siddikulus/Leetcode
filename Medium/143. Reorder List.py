'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''
from DSinitialization.data_structure_initialization import Linkedlist


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Get two lists, first till middle element, second from next to middle till end
        c1 = head
        c2head = slow.next
        c2 = c2head
        slow.next = None

        #Reverse second list
        prev = None
        while c2:
            # print(c2.val)
            nextnode = c2.next
            c2.next = prev
            prev = c2
            c2 = nextnode

        #Create new list with alternating nodes from the two lists
        dummyhead = ListNode(-1)
        dummy = dummyhead
        c2 = prev

        while c2:
            h1 = c1.next
            h2 = c2.next
            c1.next = c2
            c2.next = h1
            c1 = h1
            c2 = h2


listhead1 = Linkedlist().append([1,2,3,4,5])

head = Solution().reorderList(listhead1)

while head:
    print(head.val)
    head = head.next