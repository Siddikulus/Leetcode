'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = collections.deque()
        q.append(root)
        curr_lvl = 0
        ans = []
        while q:
            if curr_lvl%2 == 1:
                l = 0
                r = len(q) - 1
                while l<r:
                    q[l].val , q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level.append(node.val)
            if level:
                ans.append(level)
            curr_lvl+=1
        return ans

root = BinaryTree().deserialize('[3,9,20,null,null,15,7]')
# BinaryTree().drawtree(root)
print(Solution().zigzagLevelOrder(root))