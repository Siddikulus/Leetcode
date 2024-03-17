'''
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.



Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false


Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2: return True
        if not root1 or not root2: return False

        def flippy(root1, root2):
            if not root1: return None
            if not root2: return None
            if (root2.left and root1.right and root2.left.val == root1.right.val) and (root2.right and root1.left and root2.right.val == root1.left.val):
                root1.left, root1.right = root1.right, root1.left
            if (not root2.left and not root1.right) and (root1.left and root2.right and root1.left.val == root2.right.val):
                root1.left, root1.right = root1.right, root1.left
            if (not root2.right and not root1.left) and (root1.right and root2.left and root1.right.val == root2.left.val):
                root1.left, root1.right = root1.right, root1.left
            flippy(root1.left, root2.left)
            flippy(root1.right, root2.right)
        flippy(root1, root2)
        arr1 = []
        arr2 = []
        self.dfs(root1, arr1)
        self.dfs(root2, arr2)
        # print(arr1, arr2)
        return arr1 == arr2

    def dfs(self, root, arr):
        if root:
            self.dfs(root.left, arr)
            arr.append(root.val)
            self.dfs(root.right, arr)
        return root

root1 = BinaryTree().deserialize('[1]')
root2 = BinaryTree().deserialize('[1]')

print(Solution().flipEquiv(root1, root2))
# BinaryTree().drawtree(newroot1)

