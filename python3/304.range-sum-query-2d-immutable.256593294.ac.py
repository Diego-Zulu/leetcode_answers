#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (37.23%)
# Likes:    854
# Dislikes: 168
# Total Accepted:    106.3K
# Total Submissions: 285.2K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
# 
# 
# 
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
# and (row2, col2) = (4, 3), which contains sum = 8.
# 
# 
# Example:
# 
# Given matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# 
# 
# Note:
# 
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
# 
# 
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = []
        for i in range(len(matrix)):
            new_row, _sum = [], 0
            for j in range(len(matrix[0])):
                _sum += matrix[i][j]
                carried_sum = self.sum_matrix[i-1][j] if i > 0 else 0
                new_row.append(_sum + carried_sum)
            self.sum_matrix.append(new_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        start_r, start_c = min(row1, row2), min(col1, col2)
        end_r, end_c = max(row1, row2), max(col1, col2)
        result = self.sum_matrix[end_r][end_c]
        result -= self.sum_matrix[start_r - 1][end_c] if start_r > 0 else 0
        result -= self.sum_matrix[end_r][start_c - 1] if start_c > 0 else 0
        result += self.sum_matrix[start_r - 1][start_c - 1] if start_c > 0 and start_r > 0 else 0
        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
