'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.



Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]


Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        def path(root, s):
            if not root: return
            s += str(root.val) + '->'
            if not root.left and not root.right:
                ans.append(s[:-2])
            else:
                path(root.left, s)
                path(root.right, s)
        path(root, '')
        return ans

root = BinaryTree().deserialize('[1,2,7,3,4,8,9,5,6,null,null,10,null,11,12]')
BinaryTree().drawtree(root)
print(Solution().binaryTreePaths(root))