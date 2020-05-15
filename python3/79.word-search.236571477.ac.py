#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (34.26%)
# Likes:    3240
# Dislikes: 160
# Total Accepted:    433.7K
# Total Submissions: 1.3M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
# 
# Constraints:
# 
# 
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#

# @lc code=start
def out_of_bounds(r, c, board):
    return r < 0 or r >= len(board) or c < 0 or c >= len(board[0])

def dfs(r, c, pos, board, word, visited):
    if pos >= len(word):
        return True
    if (r, c) in visited or out_of_bounds(r, c, board) or word[pos] != board[r][c]:
        return False
    visited.add((r, c))
    if dfs(r+1, c, pos+1, board, word, visited) or \
    dfs(r-1, c, pos+1, board, word, visited) or \
    dfs(r, c+1, pos+1, board, word, visited) or \
    dfs(r, c-1, pos+1, board, word, visited):
        return True
    visited.remove((r, c))
    return False
    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return True
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == word[0]:
                    if dfs(r, c, 0, board, word, set()):
                        return True
        return False
# @lc code=end
