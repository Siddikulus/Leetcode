'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low_level1 = 0
        high_level1 = len(matrix)-1

        while low_level1<=high_level1:
            mid_level1 = (low_level1+high_level1)//2
            if (matrix[mid_level1][0] == target) or (matrix[mid_level1][len(matrix[mid_level1])-1] == target):
                return True

            if matrix[mid_level1][0] > target:
                high_level1 = mid_level1 - 1
            else:
                low_level1 = mid_level1 + 1

            low_level2 = 0
            high_level2 = len(matrix[mid_level1]) - 1

            while low_level2 <= high_level2:
                mid_level2 = (low_level2 + high_level2) // 2
                print(low_level1, mid_level1, high_level1, matrix[mid_level1], low_level2, mid_level2, high_level2, matrix[mid_level1][mid_level2])
                if matrix[mid_level1][mid_level2] == target:
                    return True

                if matrix[mid_level1][mid_level2] > target:
                    high_level2 = mid_level2 - 1
                elif matrix[mid_level1][mid_level2] < target:
                    low_level2 = mid_level2 + 1
                else:
                    return False

        return False

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 32))