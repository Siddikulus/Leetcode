'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counter = {0:1}
        prefix_sum = 0
        final = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            diff = prefix_sum-k
            if diff in counter:
                final += counter[diff]
            counter[prefix_sum] = 1 + counter.get(prefix_sum, 0)
        return final

print(Solution().subarraySum([1,2,3], 3))