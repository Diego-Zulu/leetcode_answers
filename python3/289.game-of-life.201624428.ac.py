#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (52.81%)
# Likes:    1617
# Dislikes: 265
# Total Accepted:    170.1K
# Total Submissions: 321.8K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
#

# @lc code=start
DEAD = 0
LIVE = 1
RULE1 = 2
RULE2 = 3
RULE3 = 4
RULE4 = 5

def inLimits(r, c, board):
    return r >= 0 and c >= 0 and r < len(board) and c < len(board[0])

def isLive(r, c, board):
    return board[r][c] in [LIVE, RULE1, RULE2, RULE3]

def countLiveNeighbours(r, c, board):
    neighbours = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if inLimits(i, j, board) and isLive(i, j, board) and (i != r or j != c):
                neighbours += 1
    
    return neighbours
    
def updateToRuleNumber(r, c, board, neighbours):
    live = board[r][c] == LIVE
    if neighbours < 2 and live:
        board[r][c] = RULE1
    elif neighbours in [2,3] and live:
        board[r][c] = RULE2
    elif neighbours > 3 and live:
        board[r][c] = RULE3
    elif neighbours == 3 and not live:
        board[r][c] = RULE4
    
def updateRuleToLiveStatus(r, c, board):
    rule = board[r][c]
    if LIVE == rule or RULE2 == rule or RULE4 == rule:
        board[r][c] = 1
    else:
        board[r][c] = 0

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for r, r_val in enumerate(board):
            for c, c_val in enumerate(r_val):
                updateToRuleNumber(r, c, board, countLiveNeighbours(r, c, board))
                
        for r, r_val in enumerate(board):
            for c, c_val in enumerate(r_val):
                updateRuleToLiveStatus(r, c, board)
        
# @lc code=end
