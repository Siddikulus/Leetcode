'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count = 1
        i = 0
        val = nums[0]
        countlist = []
        while i<len(nums):
            print(i, nums[i], val, count, countlist)
            if val + 1 in nums:
                count+=1
                val += 1
            else:
                count = 1
                val = nums[i]
                i+=1
            countlist.append(count)
        return max(countlist)+1

print(Solution().longestConsecutive([100,4,200,1,3,2]))