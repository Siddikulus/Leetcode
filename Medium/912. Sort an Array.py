'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) > 1:
            mid = len(nums)//2
            left_arr = nums[:mid]
            right_arr = nums[mid:]

            Solution().sortArray(left_arr)
            Solution().sortArray(right_arr)

            left_idx = right_idx = current_idx = 0
            while left_idx < len(left_arr) and right_idx < len(right_arr):
                if left_arr[left_idx] < right_arr[right_idx]:
                    nums[current_idx] = left_arr[left_idx]
                    left_idx += 1
                else:
                    nums[current_idx] = right_arr[right_idx]
                    right_idx += 1
                current_idx += 1

            while left_idx < len(left_arr):
                nums[current_idx] = left_arr[left_idx]
                left_idx += 1
                current_idx += 1

            while right_idx < len(right_arr):
                nums[current_idx] = right_arr[right_idx]
                right_idx += 1
                current_idx += 1

        return nums


s = Solution()
print(s.sortArray([5,2,3,1]))

