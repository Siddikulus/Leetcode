'''
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.


Example 1:


Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
Example 2:


Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:


Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]


Constraints:

The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109

'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: TreeNode
        """
        ans = []
        count = 0
        i = 0
        while i < len(traversal):
            if traversal[i] == '-':
                count += 1
                i+=1
            else:
                j = i
                s = ''
                while j < len(traversal) and traversal[j] != '-':
                    s += traversal[j]
                    j+=1
                ans.append((s, count))
                count = 0
                i = j

        # print(ans)
        nodes = [TreeNode(int(n)) for n,d in ans]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root


#Wrong

# root = BinaryTree().deserialize('[1,2,2,3,4,3,4]')
newroot = Solution().recoverFromPreorder("1-401--349---90--88")
BinaryTree().drawtree(newroot)
