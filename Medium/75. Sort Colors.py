'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]

            Solution.sortColors(self,left)
            Solution.sortColors(self,right)

            left_idx = right_idx = current = 0

            while left_idx < len(left) and right_idx < len(right):
                if left[left_idx] < right[right_idx]:
                    nums[current] = left[left_idx]
                    left_idx += 1
                else:
                    nums[current] = right[right_idx]
                    right_idx += 1
                current += 1

            while left_idx < len(left):
                nums[current] = left[left_idx]
                left_idx+=1
                current+=1

            while right_idx < len(right):
                nums[current] = right[right_idx]
                right_idx+=1
                current+=1

            return nums

print(Solution().sortColors([2,0,2,1,1,0]))