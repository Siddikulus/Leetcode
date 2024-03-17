'''
Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).



Example 1:


Input: root = [5,2,-3]
Output: [2,-3,4]
Example 2:


Input: root = [5,2,-5]
Output: [2]


Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def dfs(root):
            if not root:
                return 0
            total = root.val + dfs(root.left) + dfs(root.right)
            ans.append(total)
            return total

        dfs(root)

        counter = {}
        for element in ans:
            counter[element] = 1 + counter.get(element, 0)
        maxcount = max(counter.values())
        if maxcount == 1:
            return ans
        else:
            final = []
            for k,v in counter.items():
                if v == maxcount:
                    final.append(k)
            return final


root = BinaryTree().deserialize('[5,14,null,1]')
# BinaryTree().drawtree(root)
print(Solution().findFrequentTreeSum(root))