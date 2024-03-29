'''
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.



Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]


Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
'''
from DSinitialization.data_structure_initialization import BinaryTree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def dfs(root):
            if not root: return None
            if root.val > val and root.left:
                return dfs(root.left)
            if root.val < val and root.right:
                return dfs(root.right)
            if root.val > val and not root.left:
                root.left = TreeNode(val)
                return
            if root.val < val and not root.right:
                root.right = TreeNode(val)
                return
        if not root: return TreeNode(val)
        dfs(root)
        return root

root = BinaryTree().deserialize('[40,20,60,10,30,50,70]')
newroot = Solution().insertIntoBST(root, 25)
BinaryTree().drawtree(newroot)
