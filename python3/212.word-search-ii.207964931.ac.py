#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (32.91%)
# Likes:    2092
# Dislikes: 97
# Total Accepted:    182.6K
# Total Submissions: 554.2K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# 
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
# 
# 
# 
# Example:
# 
# 
# Input: 
# board = [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# 
# Output: ["eat","oath"]
# 
# 
# 
# 
# Note:
# 
# 
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
# 
# 
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.word = None
        self.next = [None] * (ord('z') - ord('a') + 1)
        
def buildTrie(words):
    root = TrieNode()
    for w in words:
        p = root
        for c in w:
            next_pos = ord(c) - ord('a')
            if p.next[next_pos] is None:
                p.next[next_pos] = TrieNode()
            p = p.next[next_pos]
        p.word = w
    return root

def nextPos(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
def findWordsAux(board, t, x, y, foundWords):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == '#':
        return
    c = board[x][y]
    t = t.next[ord(c) - ord('a')]
    if t:   
        if t.word:
            foundWords.append(t.word)
            t.word = None
        board[x][y] = '#'
        for p in nextPos(x, y):
            findWordsAux(board, t, p[0], p[1], foundWords)
        board[x][y] = c

class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        t = buildTrie(words)
        foundWords = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                findWordsAux(board, t, i, j, foundWords)
        return foundWords
# @lc code=end
