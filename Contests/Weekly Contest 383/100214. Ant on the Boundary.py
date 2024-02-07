''' bkoi00='''


class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        boundary = 0
        count = 0
        for ant in nums:
            boundary = boundary + ant
            if boundary == 0:
                count = count + 1
        return count


print(Solution().returnToBoundaryCount(nums = [3,5,-15,2]))