#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (50.90%)
# Likes:    235
# Dislikes: 1017
# Total Accepted:    46.3K
# Total Submissions: 90.9K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D integer matrix M representing the gray scale of an image, you need
# to design a smoother to make the gray scale of each cell becomes the average
# gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
# cell has less than 8 surrounding cells, then use as many as you can.
# 
# Example 1:
# 
# Input:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# Output:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# 
# 
# 
# Note:
# 
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
# 
# 
#

# @lc code=start
def surroundingPos(r, c, n, m):
    l_r = r-1 if r-1 > 0 else r
    r_r = r+1 if r+1 <= n else r
    l_c = c-1 if c-1 > 0 else c
    r_c = c+1 if c+1 <= m else c
    
    return (r_r - l_r + 1) * (r_c - l_c + 1)


def getPosSmoothedValue(M, r, c, n, m):
    sum_val = 0
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            sum_val += M[i][j]
    return math.floor(sum_val / surroundingPos(r, c, n, m))


class Solution:
    def imageSmoother(self, M):
        if not M:
            return M
        n = len(M)
        m = len(M[0])
        M = [[0] + row + [0] for row in M]
        M = [[0] * (m + 2)] + M + [[0] * (m + 2)]
        smoothed = []
        for r in range(1, n + 1):
            smoothed_row = []
            for c in range(1, m + 1):
                smoothed_row.append(getPosSmoothedValue(M, r, c, n, m))
            smoothed.append(smoothed_row)
        return smoothed
# @lc code=end
