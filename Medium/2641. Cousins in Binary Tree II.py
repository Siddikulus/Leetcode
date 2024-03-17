'''
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.



Example 1:


Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
Example 2:


Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.


Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 104

'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        relation = {}
        relation[root.val] = (None, 0)
        def dfs(root, depth):
            if not root: return None
            if root.left:
                relation[root.left.val] = (root, depth+1)
            if root.right:
                relation[root.right.val] = (root, depth+1)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)

        root.val = 0
        def dfs2(root, depth):
            if not root: return None
            if root.left:
                total = 0
                for key, vals in relation.items():
                    if key != root.left.val:
                        if vals[1] == depth+1 and vals[0]!=root:
                            total+=key
                root.left.val = total

            if root.right:
                total = 0
                for key, vals in relation.items():
                    if key != root.right.val:
                        if vals[1] == depth+1 and vals[0]!=root:
                            total+=key
                root.right.val = total

            dfs2(root.left, depth+1)
            dfs2(root.right, depth+1)
        dfs2(root, 0)
        return root

root = BinaryTree().deserialize('[904,416,765,705,null,null,14,null,null,821,754,774,30,null,548,905,879,363,130,494,null,null,451,327,414,null,null,null,null,41,null,471,null,703,null,null,null,null,null,574,null,41,895,null,214,null,365]')
BinaryTree().drawtree(root)
newroot = Solution().replaceValueInTree(root)
