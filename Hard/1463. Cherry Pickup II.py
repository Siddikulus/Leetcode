'''
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.


Example 1:


Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
Example 2:


Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.


Constraints:

rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100

'''


class Solution(object):
    def cherryPickup(self, grid):

        rows, cols = len(grid), len(grid[0])

        # Define a memoization dictionary to store already calculated results
        memo = {}

        def dp(r, c1, c2):
            # Base case: If robots go out of bounds or reach the top row, return 0
            if r == rows or c1 < 0 or c1 == cols or c2 < 0 or c2 == cols:
                return 0

            # Check if the result for this state has already been calculated
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]

            # Collect cherries from the current cells
            cherries = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)

            # Calculate the maximum cherries collected by both robots in the next row
            max_cherries = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    max_cherries = max(max_cherries, dp(r + 1, c1 + dc1, c2 + dc2))

            # Add the cherries collected from the current cell to the maximum cherries from the next row
            result = cherries + max_cherries

            # Memoize the result
            memo[(r, c1, c2)] = result

            return result

        # Start the dynamic programming process from the top row and return the result
        return dp(0, 0, cols - 1)

#Full Referenced - DP