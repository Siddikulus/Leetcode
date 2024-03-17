'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count = {0:0, 1:0}
        left = 0
        right = 0
        maxlen = 0
        while right < len(nums):
            count[nums[right]] = 1 + count[nums[right]]

            while count[0] == count[1]:
                maxlen = max(maxlen, right - left + 1)
                count[nums[left]] = count[nums[left]] - 1
                left += 1
            right += 1
        return maxlen
print(Solution().findMaxLength(nums = [0,1,0]))