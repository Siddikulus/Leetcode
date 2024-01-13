'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.


Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''


class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        iterations = max(rows,cols)
        count = 0
        for size in range(iterations-1):
            for i in range(rows):
                for j in range(cols):
                    if j+size < cols and i+size<rows:
                        # print(size, i,j,count, matrix[i][j], matrix[i][j+size], matrix[i+size][j], matrix[i+size][j+size])
                        if matrix[i][j] == 1 and matrix[i][j+size] == 1 and matrix[i+size][j] == 1 and matrix[i+size][j+size] == 1:
                            count+=1
        return count

#Wrong answer - couldn't solve

print(Solution().countSquares(matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]))


