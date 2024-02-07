'''
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.



Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.


Constraints:

1 <= n <= 1000
0 <= k <= 1000
'''


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7  # Define the modulus value to keep numbers within integer bounds

        # dp table representing the count of inverse pairs for the current number of integers
        dp = [1] + [0] * k

        # Prefix sum array for optimization of the inner loop. The size is k+2 for 1-indexed and ease of access
        prefix_sum = [0] * (k + 2)

        # Iterate through integers from 1 to n
        for current_number in range(1, n + 1):
            # Going through all possible counts of inverse pairs from 1 to k
            for inverse_count in range(1, k + 1):
                # Update the dp table by taking the count from the prefix_sum within the range
                # The range corresponds to the valid inverse pair counts that can be formed with the current number
                dp[inverse_count] = (prefix_sum[inverse_count + 1] -
                                     prefix_sum[max(0, inverse_count - (current_number - 1))]) % mod

            # Updating prefix_sum based on the updated dp table
            for index in range(1, k + 2):
                prefix_sum[index] = (prefix_sum[index - 1] + dp[index - 1]) % mod

        # Returning the number of ways to form k inverse pairs with n integers
        return dp[k]

#Full referenced