'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.



Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]


Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if not root: return None
        ans = []
        def dfs(root):
            # print(root.val)
            if not root: return None
            dfs(root.left)
            dfs(root.right)

            if root.val in to_delete:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                return None
            else:
                return
        dfs(root)
        return ans + [root]


root = BinaryTree().deserialize('[1,2,3,4,5,6,7]')
# BinaryTree().drawtree(root)
print(Solution().delNodes(root, [3,5]))