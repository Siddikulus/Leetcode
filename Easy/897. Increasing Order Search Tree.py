'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.



Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]


Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ans = []
        def inorder(root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
        inorder(root)
        newroot = TreeNode(ans[0])
        curr = newroot
        for i in range(1, len(ans)):
            curr.right = TreeNode(ans[i])
            curr = curr.right
        return newroot

root = BinaryTree().deserialize('[1,2,7,3,4,8,9,5,6,null,null,10,null,11,12]')
# BinaryTree().drawtree(root)

print(Solution().increasingBST(root))