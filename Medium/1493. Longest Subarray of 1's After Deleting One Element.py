'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        i,j,max_length = 0,0,0
        element_count = {0:0, 1:0}

        while i < len(nums) and j<len(nums):
            element_count[nums[j]] = 1 + element_count.get(nums[j], 0)
            # print(nums, i, j, element_count, max_length)
            if element_count[0] > 1:
                element_count[nums[i]] -= 1
                i+=1
            max_length = max(max_length, j-i)
            j+=1

        return max_length

print(Solution().longestSubarray([1,1,1]))