'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''

from functools import cmp_to_key
class Solution:

    def largestNumber(self, nums: list[int]) -> str:
        nums[:] = [str(x) for x in nums]

        def comparison(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1

        nums = sorted(nums, key = cmp_to_key(comparison))
        return str(int(''.join(nums)))

print(Solution().largestNumber([3,30,34,5,9]))