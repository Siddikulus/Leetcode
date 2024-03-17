'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.



Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

'''

from DSinitialization.data_structure_initialization import BinaryTree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0: return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums)//2
        leftarr = nums[:mid]
        rightarr = nums[mid+1:]
        root = TreeNode(nums.pop(mid))
        root.left = self.sortedArrayToBST(leftarr)
        root.right = self.sortedArrayToBST(rightarr)
        return root


# root = BinaryTree().deserialize('[1,2,2,3,4,3,4]')
root = Solution().sortedArrayToBST([-10,-3,0,5,9])
BinaryTree().drawtree(root)