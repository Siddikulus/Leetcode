'''
Given the root of a binary tree, return the sum of values of its deepest leaves.


Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            qlen = len(queue)
            level = []
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            if level:
                ans.append(level)
        return sum(ans[-1])


root = BinaryTree().deserialize('[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]')
# BinaryTree().drawtree(root)
print(Solution().deepestLeavesSum(root))