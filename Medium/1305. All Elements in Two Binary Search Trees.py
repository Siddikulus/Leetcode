'''
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.



Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]


Constraints:

The number of nodes in each tree is in the range [0, 5000].
-105 <= Node.val <= 105
'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def dfs(root, arr):
            if root:
                dfs(root.left, arr)
                arr.append(root.val)
                dfs(root.right, arr)
            return arr

        arr1 = []
        arr2 = []
        arr1 = dfs(root1, arr1)
        arr2 = dfs(root2, arr2)

        return sorted(arr1+arr2)

root1 = BinaryTree().deserialize('[2,1,4]')
root2 = BinaryTree().deserialize('[1,0,3]')

# BinaryTree().drawtree(root)
print(Solution().getAllElements(root1, root2))