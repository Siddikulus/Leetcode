'''
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []
        def dfs(root):
            if not root: return None
            if root.left is not None:
                print(root.val, root.left.val, ans)
                if root.left.left == None and root.left.right == None:
                    ans.append(root.left.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        # print(ans)
        return sum(ans)



root = BinaryTree().deserialize('[1]')
# BinaryTree().drawtree(root)
print(Solution().sumOfLeftLeaves(root))
