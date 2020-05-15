#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (53.28%)
# Likes:    2694
# Dislikes: 55
# Total Accepted:    395.7K
# Total Submissions: 742.3K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#

# @lc code=start
import sys

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for c in range(1, m):
            grid[0][c] += grid[0][c-1]
        for r in range(1, n):
            for c in range(m):
                up = grid[r][c-1] if c > 0 else sys.maxsize
                left = grid[r-1][c] if r > 0 else sys.maxsize
                grid[r][c] += min(up, left)
        return grid[n-1][m-1]
# @lc code=end
