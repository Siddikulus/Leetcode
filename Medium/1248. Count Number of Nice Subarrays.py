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

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:

        #Wrong, could not understand question
        # countParity = {'odd':0, 'even': 0}
        # i = 0
        # j = 0
        # count = 0
        # while i<len(nums) and j<len(nums):
        #     if nums[j]%2 == 0:
        #         countParity['even'] += 1
        #     else:
        #         countParity['odd'] += 1
        #
        #     while countParity['odd'] == k:
        #         print(nums[i:j+1], i, j, count)
        #         count+=1
        #         if nums[i] % 2 == 0:
        #             countParity['even'] -= 1
        #         else:
        #             countParity['odd'] -= 1
        #     j+=1
        #     # print(nums[i:j + 1], i, j, count)
        # return count
        pass

print(Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))
