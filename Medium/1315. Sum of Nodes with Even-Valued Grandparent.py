'''
Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.



Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
Example 2:


Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100

'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.totalsum = 0

    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if root.val%2 == 0:
            if root.left:
                if root.left.left:
                    self.totalsum += root.left.left.val
                if root.left.right:
                    self.totalsum += root.left.right.val
            if root.right:
                if root.right.left:
                    self.totalsum += root.right.left.val
                if root.right.right:
                    self.totalsum += root.right.right.val

        self.sumEvenGrandparent(root.left)
        self.sumEvenGrandparent(root.right)
        return self.totalsum

root = BinaryTree().deserialize('[1]')
# BinaryTree().drawtree(root)
print(Solution().sumEvenGrandparent(root))