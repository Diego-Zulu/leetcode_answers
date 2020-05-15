#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (42.47%)
# Likes:    1811
# Dislikes: 285
# Total Accepted:    296.6K
# Total Submissions: 698.3K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#

# @lc code=start
def mark_row(matrix, r):
    for c in range(len(matrix[0])):
        matrix[r][c] = 0
        
def mark_col(matrix, c):
    for r in range(len(matrix)):
        matrix[r][c] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell == 0:
                    row[0] = 0
                    matrix[0][c] = 0
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                mark_row(matrix, r)
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                mark_col(matrix, c)
        if matrix[0][0] == 0:
            mark_row(matrix, 0)
            mark_col(matrix, 0)
# @lc code=end
