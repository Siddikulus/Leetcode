'''
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.



Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100
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
        self.prev = None
        self.count = 0

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            self.isUnivalTree(root.left)
            if root.val != self.prev:
                self.count += 1
            self.prev = root.val
            self.isUnivalTree(root.right)
        return self.count == 1


root = BinaryTree().deserialize('[2,2,2,5,2]')
# BinaryTree().drawtree(root)
print(Solution().isUnivalTree(root))