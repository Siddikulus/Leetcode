'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.



Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
'''
from DSinitialization.data_structure_initialization import BinaryTree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root and root.val == val:
            return root
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        elif root and val < root.val:
            return self.searchBST(root.left, val)
        else:
            return None

root = BinaryTree().deserialize('[4,2,7,1,3]')
# BinaryTree().drawtree(root)
print(Solution().searchBST(root, 17))