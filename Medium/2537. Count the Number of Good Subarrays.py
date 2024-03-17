'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.


Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 109

'''


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        count = {}
        left = 0
        right = 0
        total = 0
        pairs = 0
        while right < len(nums):
            count[nums[right]] = 1 + count.get(nums[right], 0)
            pairs += count[nums[right]] - 1
            while pairs >= k:
                total += len(nums) - right
                count[nums[left]] = count[nums[left]] - 1
                pairs = pairs - count[nums[left]]
                left += 1
            right += 1
        return total
print(Solution().countGood(nums = [1,1,1,1,1], k = 10))