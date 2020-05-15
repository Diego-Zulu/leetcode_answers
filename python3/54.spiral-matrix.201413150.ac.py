#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (33.31%)
# Likes:    2081
# Dislikes: 538
# Total Accepted:    345.7K
# Total Submissions: 1M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#

# @lc code=start
from typing import List

N: int = 0
E: int = 1
S: int = 2
W: int = 3
    
def move(direction: int, pos: tuple) -> tuple:
    if direction == N: return (pos[0] - 1, pos[1])
    elif direction == E: return (pos[0], pos[1] + 1)
    elif direction == S: return (pos[0] + 1, pos[1])
    else: return (pos[0], pos[1] - 1)
    
def border_reached(direction: int, pos: tuple, loop: int, matrix: List[List[int]]) -> bool:
    if direction == N: return pos[0] == loop
    elif direction == E: return pos[1] == len(matrix[0]) - loop - 1
    elif direction == S: return pos[0] == len(matrix) - loop - 1
    else: return pos[1] == loop

def next_direction(direction: int) -> int:
    return (direction + 1) % 4

class Solution:
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        count: int = 0
        output: List[int] = []
        total_elements = len(matrix) * len(matrix[0]) if matrix else 0
        pos = (0,0)
        direction = E
        loop = 0
        
        while count < total_elements:
            output.append(matrix[pos[0]][pos[1]])
            count += 1
            
            if border_reached(direction, pos, loop, matrix):
                direction = next_direction(direction)
                if direction == N:
                    loop += 1
            pos = move(direction, pos)
        
        return output
            
        
# @lc code=end
