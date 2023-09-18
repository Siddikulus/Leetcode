'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        slow = 0
        while slow<len(nums):
            for fast in range(1,len(nums)):
                if slow!=fast and nums[slow] == nums[fast] and (abs(fast-slow) <= k):
                    print(nums[slow], nums[fast])
                    print(slow,fast)
                    return True
            slow+=1
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))