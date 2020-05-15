#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (45.88%)
# Likes:    4996
# Dislikes: 189
# Total Accepted:    676.1K
# Total Submissions: 1.5M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

# @lc code=start
def delete_island(grid, r, c):
    dfs = [(r, c)]
    while len(dfs) > 0:
        curr_r, curr_c = dfs.pop()
        if curr_r < 0 or curr_r == len(grid) or curr_c < 0 or curr_c == len(grid[0]) or grid[curr_r][curr_c] == "0":
            continue
        grid[curr_r][curr_c] = "0"
        dfs.append((curr_r + 1, curr_c))
        dfs.append((curr_r, curr_c + 1))
        dfs.append((curr_r - 1, curr_c))
        dfs.append((curr_r, curr_c - 1))

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    delete_island(grid, r, c)
                    num += 1
        return num
# @lc code=end
