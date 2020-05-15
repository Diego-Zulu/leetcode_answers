#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (47.34%)
# Likes:    662
# Dislikes: 318
# Total Accepted:    76.3K
# Total Submissions: 161K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#

# @lc code=start
def downDiagonal(r, c, n, m):
    if r == 0 and c < m - 1:
        change()
        return r, c + 1
    elif c == m - 1:
        change()
        return r + 1, c
    else:
        return r - 1, c + 1


def upDiagonal(r, c, n, m):
    if c == 0 and r < n - 1:
        change()
        return r + 1, c
    elif r == n - 1:
        change()
        return r, c + 1
    else:
        return r + 1, c - 1


UNUSED_ADVANCE = upDiagonal
ADVANCE_FUNCTION = downDiagonal


def change():
    global UNUSED_ADVANCE
    global ADVANCE_FUNCTION
    ADVANCE_FUNCTION, UNUSED_ADVANCE = UNUSED_ADVANCE, ADVANCE_FUNCTION


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix: return []
        global UNUSED_ADVANCE
        global ADVANCE_FUNCTION
        UNUSED_ADVANCE = upDiagonal
        ADVANCE_FUNCTION = downDiagonal
        n = len(matrix)
        m = len(matrix[0])
        res = []
        left = n * m
        pos = 0, 0
        while left:
            left -= 1
            res.append(matrix[pos[0]][pos[1]])
            pos = ADVANCE_FUNCTION(pos[0], pos[1], n, m)
        return res
# @lc code=end
