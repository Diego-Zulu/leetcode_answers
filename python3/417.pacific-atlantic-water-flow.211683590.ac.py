#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (40.17%)
# Likes:    1099
# Dislikes: 222
# Total Accepted:    69.2K
# Total Submissions: 172.2K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# 
# 
# Example:
# 
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
# 
# 
#

# @lc code=start
def moves(r, c, playfield, matrix, n, m):
    if r + 1 < n and not playfield[r+1][c] and matrix[r][c] <= matrix[r+1][c]:
        yield r+1, c
    if c + 1 < m and not playfield[r][c+1] and matrix[r][c] <= matrix[r][c+1]:
        yield r, c+1
    if r - 1 >= 0 and not playfield[r-1][c] and matrix[r][c] <= matrix[r-1][c]:
        yield r-1, c
    if c - 1 >= 0 and not playfield[r][c-1] and matrix[r][c] <= matrix[r][c-1]:
        yield r, c-1

def dfs(r, c, playfield, matrix, n, m):
    playfield[r][c] = True
    for next_r, next_c in moves(r, c, playfield, matrix, n, m):
        dfs(next_r, next_c, playfield, matrix, n, m)

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        n = len(matrix)
        m = len(matrix[0])
        atlantic = [[False] * m for _ in range(n)]
        pacific = [[False] * m for _ in range(n)]
        for i in range(n):
            dfs(i, m - 1, atlantic, matrix, n, m)
            dfs(i, 0, pacific, matrix, n, m)
        for i in range(m):
            dfs(n - 1, i, atlantic, matrix, n, m)
            dfs(0, i, pacific, matrix, n, m)
        result = []
        for r in range(n):
            for c in range(m):
                if atlantic[r][c] and pacific[r][c]:
                    result.append((r, c))
        return result
# @lc code=end
