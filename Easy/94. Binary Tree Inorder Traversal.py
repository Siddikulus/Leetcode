'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
'''

from DSinitialization.data_structure_initialization import BinaryTree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # #Recursive
        # ans = []
        # def dfs(node):
        #     if node:
        #         dfs(node.left)
        #         ans.append(node.val)
        #         dfs(node.right)
        # dfs(root)
        # return ans

        #Iterative
        ans = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right

        return ans

root = BinaryTree().deserialize('[1,2,7,3,4,8,9,5,6,null,null,10,null,11,12]')
# BinaryTree().drawtree(root)
print(Solution().inorderTraversal(root))