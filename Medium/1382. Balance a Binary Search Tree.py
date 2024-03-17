'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.



Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
'''
from DSinitialization.data_structure_initialization import BinaryTree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def dfs(self, root):
        ans = []
        def helper(root):
            if root:
                helper(root.left)
                ans.append(root.val)
                helper(root.right)
        helper(root)
        return ans
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        vals = self.dfs(root)
        root = self.createBST(vals)

        return root

    def createBST(self, arr):
        if len(arr) == 0: return None
        if len(arr) == 1: return TreeNode(arr[0])

        mid = len(arr)//2
        leftarr = arr[:mid]
        rightarr = arr[mid+1:]

        root = TreeNode(arr.pop(mid))
        root.left = self.createBST(leftarr)
        root.right = self.createBST(rightarr)
        return root

root = BinaryTree().deserialize('[1,2,2,3,4,3,4]')
newroot = Solution().balanceBST(root)
BinaryTree().drawtree(newroot)
