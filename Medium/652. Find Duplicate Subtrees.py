'''
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.



Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]


Constraints:

The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        count = defaultdict(list)
        ans = []
        def dfs(root):
            if not root:
                return 'null'

            s = ','.join([str(root.val), dfs(root.left), dfs(root.right)])
            if len(count[s]) == 1:
                ans.append(root)
            count[s].append(root)
            return s
        dfs(root)
        return ans


root = BinaryTree().deserialize('[1,2,3,4,null,2,4,null,null,4]')
# BinaryTree().drawtree(root)
print(Solution().findDuplicateSubtrees(root))