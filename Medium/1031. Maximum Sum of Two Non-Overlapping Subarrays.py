'''
Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.


Constraints:

1 <= firstLen, secondLen <= 1000
2 <= firstLen + secondLen <= 1000
firstLen + secondLen <= nums.length <= 1000
0 <= nums[i] <= 1000
'''


class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        firstmax, firstsubarr =  self.maxconsecutivesum(nums, firstLen)
        print(firstsubarr)
        newnums = ''.join([str(x) for x in nums]).replace(''.join([str(i) for i in firstsubarr]), '')
        seconditer = [int(x) for x in list(newnums)]
        print(seconditer)

        secondmax, secondsubarr = self.maxconsecutivesum(seconditer, secondLen)
        print(secondsubarr)
        return firstmax + secondmax

    def maxconsecutivesum(self, nums: list[int], k: int) -> tuple:
        left = 0
        right = 0
        maxval = 0
        totalval = 0
        maxsubarr = {}
        while right < len(nums):
            totalval += nums[right]

            while (right-left+1) == k:
                maxsubarr[totalval] = nums[left:right+1]
                maxval = max(maxval, totalval)
                totalval -= nums[left]
                left+=1

            right += 1
        return maxval, maxsubarr[maxval]

print(Solution().maxSumTwoNoOverlap(nums = [1,0,1], firstLen = 1, secondLen = 1))