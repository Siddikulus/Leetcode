'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.

'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder: return None
        if len(postorder) == 1: return TreeNode(postorder[0])
        rootval = postorder.pop()
        # print(rootval, postorder, inorder)
        root = TreeNode(rootval)
        index = inorder.index(rootval)
        left = inorder[:index]
        right = inorder[index+1:]
        if right:
            root.right = self.buildTree(right, postorder)
        if left:
            root.left = self.buildTree(left, postorder)
        return root

root = Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
BinaryTree().drawtree(root)
