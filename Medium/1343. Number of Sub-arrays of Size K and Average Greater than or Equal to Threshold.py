'''
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.



Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.


Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 104
1 <= k <= arr.length
0 <= threshold <= 104
'''


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        i = 0
        j = 0
        count = 0
        sumnums = 0
        while j < len(arr):
            win_size = j-i+1
            sumnums = sumnums + arr[j]

            if win_size == k:
                if sumnums/k >= threshold:
                    count+=1
                # print(arr, i, j, arr[i], arr[j], sumnums)
                sumnums -= arr[i]
                i += 1
                j += 1

            else:
                j += 1
        return count


print(Solution().numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))