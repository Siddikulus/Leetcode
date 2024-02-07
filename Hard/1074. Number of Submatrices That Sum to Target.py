'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.



Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0


Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
'''


class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]
            mat[i] = [0] + mat[i]
        ans = 0
        d = defaultdict(int)
        for col1 in range(n):
            for col2 in range(col1 + 1, n + 1):
                temp = 0
                d[0] = 1
                for r in range(m):
                    temp += mat[r][col2] - mat[r][col1]
                    if (temp - target in d):
                        ans += d[temp - target]
                    d[temp] += 1
                d.clear()
        return ans

#Full referenced