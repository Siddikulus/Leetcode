'''
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

from DSinitialization.data_structure_initialization import BinaryTree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(root):
            if not root: return 0
            left = helper(root.left)
            right = helper(root.right)
            if left == -1: return -1
            if right == -1: return -1
            if abs(left-right) > 1:
                return -1
            return 1+max(left, right)

        return helper(root) != -1


root = BinaryTree().deserialize('[null]')
# BinaryTree().drawtree(root)
print(Solution().isBalanced(root))
