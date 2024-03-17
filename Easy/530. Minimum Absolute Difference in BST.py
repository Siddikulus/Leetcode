'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105


Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/


'''

from DSinitialization.data_structure_initialization import BinaryTree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mindiff = []
        def dfs(root):
            if root:
                dfs(root.left)
                mindiff.append(root.val)
                dfs(root.right)
        dfs(root)
        for i in range(1, len(mindiff)):
            mindiff[i-1] = mindiff[i] - mindiff[i-1]
        return min(mindiff)


root = BinaryTree().deserialize('[1,0,48,null,null,12,49]')
# BinaryTree().drawtree(root)
print(Solution().getMinimumDifference(root))
