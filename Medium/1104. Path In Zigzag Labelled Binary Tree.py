'''
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.



Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]


Constraints:

1 <= label <= 10^6
'''

from DSinitialization.data_structure_initialization import BinaryTree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from math import log2, floor


class Solution(object):
    #TLE
    # def pathInZigZagTree(self, label):
    #     """
    #     :type label: int
    #     :rtype: List[int]
    #     """
    #     #Get Level order traversal going zigzag
    #     level = 0
    #     nodesum = 0
    #     while nodesum < label:
    #         nodesum += pow(2, level)
    #         level+=1
    #     ans = []
    #     prev = 1
    #     for i in range(level):
    #         nodes = pow(2,i)
    #         nodelist = list(range(prev, nodes+prev))
    #         prev += nodes
    #         ans.append(nodelist)
    #     for i in range(len(ans)):
    #         if i%2 == 1:
    #             ans[i] = ans[i][::-1]
    #
    #     #Flatten level order traversal
    #     level_order = []
    #     for arr in ans:
    #         for element in arr:
    #             level_order.append(element)
    #
    #     string = str(level_order)
    #
    #     #Create Binary Tree from Level Order Traversal
    #     if string == '{}':
    #         return None
    #     nodes = [None if val == 'null' else TreeNode(int(val))
    #              for val in string.strip('[]{}').split(',')]
    #     kids = nodes[::-1]
    #     root = kids.pop()
    #     for node in nodes:
    #         if node:
    #             if kids: node.left = kids.pop()
    #             if kids: node.right = kids.pop()
    #
    #     paths = []
    #     def path(root, s):
    #         if not root: return
    #         s+=str(root.val)+','
    #         if not root.left and not root.right:
    #             paths.append(s)
    #         if root.left:
    #             path(root.left, s)
    #         if root.right:
    #             path(root.right, s)
    #     path(root, '')
    #
    #     for element in paths:
    #         if str(label) in element:
    #             val = element.split(',')[:-1]
    #     return [int(x) for x in val]

    def pathInZigZagTree(self, label):
        level = floor(log2(label))
        ans = [label]
        while label != 1:
            c = label - 2 ** level
            pos = c // 2
            if level & 1:
                label = 2 ** (level - 1) + (2 ** (level - 1) - pos - 1)
            else:
                label = 2 ** (level) - 1 - pos
            level -= 1
            ans.append(label)
        return ans[::-1]


# root = BinaryTree().deserialize('[1,2,2,3,4,3,4]')
root = Solution().pathInZigZagTree(26)
print(root)
# BinaryTree().drawtree(root)
