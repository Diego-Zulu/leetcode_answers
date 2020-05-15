#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (26.08%)
# Likes:    1356
# Dislikes: 588
# Total Accepted:    200.5K
# Total Submissions: 768K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#

# @lc code=start
def inside(r, c, board):
    return r >= 0 and c >= 0 and r < len(board) and c < len(board[0])

def next_pos(r, c, board):
    for i in [1, -1]:
        if inside(r+i, c, board) and board[r+i][c] == 'O':
            yield r+i, c
        if inside(r, c+i, board) and board[r][c+i] == 'O':
            yield r, c+i

def mark_as_live(r, c, board):
    dfs = [(r, c)]
    while dfs:
        curr_r, curr_c = dfs.pop()
        if board[curr_r][curr_c] in ['X', 'E']:
            continue
        board[curr_r][curr_c] = 'E'
        dfs.extend(next_pos(curr_r, curr_c, board))

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board

        for r in range(len(board)):
            for c in [0, len(board[0]) - 1]:
                if board[r][c] == 'O':
                    mark_as_live(r, c, board)
            
        for c in range(len(board[0])):
            for r in [0, len(board) - 1]:
                if board[r][c] == 'O':
                    mark_as_live(r, c, board)
                    
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'E':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
# @lc code=end
