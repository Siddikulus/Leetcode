'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.



Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15


Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
'''

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix = 0
        count = 0
        dict = {0:1}

        for i in range(len(nums)):
            prefix += nums[i]
            diff = prefix - goal
            if diff in dict:
                count+=dict[diff]
            dict[prefix] = 1 + dict.get(prefix, 0)
        return count


print(Solution().numSubarraysWithSum([0,0,0,0,0], 0))
