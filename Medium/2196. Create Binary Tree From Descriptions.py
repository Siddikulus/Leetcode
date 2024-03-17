'''
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.



Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.


Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
'''

from DSinitialization.data_structure_initialization import BinaryTree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        hashmap = {}
        nodes = set()
        children = set()
        for parent, child, isLeft in descriptions:
            nodes.add(parent)
            nodes.add(child)
            children.add(child)
            if parent not in hashmap:
                hashmap[parent] = TreeNode(parent)
            if child not in hashmap:
                hashmap[child] = TreeNode(child)
            if isLeft:
                hashmap[parent].left = hashmap[child]
            if not isLeft:
                hashmap[parent].right = hashmap[child]

        for node in nodes:
            if node not in children:
                return hashmap[node]



# root = BinaryTree().deserialize('[3,0,0]')
root = Solution().createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
BinaryTree().drawtree(root)
