'''
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.



Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.
Example 2:

Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
'''


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        class Solution:
            def findMaxLength(self, nums: List[int]) -> int:

                partial_sum = 0

                # table is a dictionary
                # key : partial sum value
                # value : the left-most index who has the partial sum value

                table = {0: -1}

                max_length = 0

                for idx, number in enumerate(nums):

                    # partial_sum add 1 for 1
                    # partial_sum minus 1 for 0

                    if number:
                        partial_sum += 1
                    else:
                        partial_sum -= 1

                    if partial_sum in table:

                        # we have a subarray with equal number of 0 and 1
                        # update max length

                        max_length = max(max_length, (idx - table[partial_sum]))

                    else:
                        # update the left-most index for specified partial sum value
                        table[partial_sum] = idx

                return max_length

#Full referenced

print(Solution().longestNiceSubarray([1,3,8,48,10]))