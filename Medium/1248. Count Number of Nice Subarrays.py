'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.



Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''


'''
# Just keep count of the current odd number.
# Look in the dictionary if we can find (currendOds - k), 
# if it exisits that means I can get an subarray with k odds.
# Also keep count of number of different types of odds too,
# because for K =1 , [2,2,1] is a valid list, so does, [2,1] and [1].


https://www.youtube.com/watch?v=xvNwoz-ufXA
'''
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        temp = nums.copy()
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                temp[i] = 0
            else:
                temp[i] = 1

        counter = {0:1}
        prefix_sum = 0
        final = 0
        for i in range(len(temp)):
            prefix_sum += temp[i]
            diff = prefix_sum-k
            if diff in counter:
                final += counter[diff]
            counter[prefix_sum] = 1 + counter.get(prefix_sum, 0)
        return final


print(Solution().numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
