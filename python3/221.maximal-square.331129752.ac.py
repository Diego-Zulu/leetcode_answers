#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (37.09%)
# Likes:    2753
# Dislikes: 71
# Total Accepted:    246K
# Total Submissions: 663.1K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maximal = 0
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if c - 1 < 0 or r - 1 < 0 or cell == '0':
                    matrix[r][c] = int(cell)
                else:
                    matrix[r][c] = 1 + min(matrix[r][c-1], matrix[r-1][c], matrix[r-1][c-1])
                maximal = max(maximal, matrix[r][c]**2)
        return maximal
                
                
# @lc code=end
