'''
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.



Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
'''
from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        ans = []
        def path(root, s):
            if not root: return
            s+=str(root.val)
            if not root.left and not root.right:
                ans.append(s)
            else:
                path(root.left, s)
                path(root.right, s)
        path(root, '')
        totalsum = 0
        for elem in ans:
            totalsum+=int(elem, 2)
        return totalsum


root = BinaryTree().deserialize('[1,0,1,0,1,0,1]')
# BinaryTree().drawtree(root)
print(Solution().sumRootToLeaf(root))