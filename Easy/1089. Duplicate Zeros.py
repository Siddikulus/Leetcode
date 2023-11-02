'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.



Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
'''


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        fin_len = len(arr)
        while i<len(arr):
            # print(i, arr[i])
            if arr[i] == 0:
                arr.insert(i+1,0)
                i+=2
            else:
                i+=1
        arr[:] = arr[:fin_len]

        return arr

print(Solution().duplicateZeros([0,4,1,0,0,8,0,0,3]))


