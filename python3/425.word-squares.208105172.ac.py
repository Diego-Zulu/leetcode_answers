#
# @lc app=leetcode id=425 lang=python3
#
# [425] Word Squares
#
# https://leetcode.com/problems/word-squares/description/
#
# algorithms
# Hard (47.30%)
# Likes:    497
# Dislikes: 38
# Total Accepted:    34.3K
# Total Submissions: 72.4K
# Testcase Example:  '["area","lead","wall","lady","ball"]'
#
# Given a set of words (without duplicates), find all word squares you can
# build from them.
# 
# A sequence of words forms a valid word square if the k^th row and column read
# the exact same string, where 0 ≤ k < max(numRows, numColumns).
# 
# For example, the word sequence ["ball","area","lead","lady"] forms a word
# square because each word reads the same both horizontally and vertically.
# 
# 
# b a l l
# a r e a
# l e a d
# l a d y
# 
# 
# Note:
# 
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# 
# 
# 
# Example 1:
# 
# Input:
# ["area","lead","wall","lady","ball"]
# 
# Output:
# [
# ⁠ [ "wall",
# ⁠   "area",
# ⁠   "lead",
# ⁠   "lady"
# ⁠ ],
# ⁠ [ "ball",
# ⁠   "area",
# ⁠   "lead",
# ⁠   "lady"
# ⁠ ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).
# 
# 
# 
# Example 2:
# 
# Input:
# ["abat","baba","atan","atal"]
# 
# Output:
# [
# ⁠ [ "baba",
# ⁠   "abat",
# ⁠   "baba",
# ⁠   "atan"
# ⁠ ],
# ⁠ [ "baba",
# ⁠   "abat",
# ⁠   "baba",
# ⁠   "atal"
# ⁠ ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).
# 
# 
#

# @lc code=start
class Trie:
    def __init__(self):
        self.word = None
        self.next = dict()
        self.next_words = []


def buildTrie(words):
    root = Trie()
    for w in words:
        p = root
        for c in w:
            p.next_words.append(w)
            if c not in p.next:
                p.next[c] = Trie()
            p = p.next[c]
        p.word = w
    return root


def wordSquaresAux(square, letters, t, square_l, possible_squares):
    root = t
    for l in letters:
        t = t.next.get(l, None)
        if t is None:
            break
    if t and len(square) < square_l - 1:
        letters = []
        for s in square:
            letters.append(s[len(square) + 1])
        for w in t.next_words:
            square.append(w)
            letters.append(w[len(square)])
            wordSquaresAux(square, letters, root, square_l, possible_squares)
            square.pop()
            letters.pop()
    elif t:
        for w in t.next_words:
            possible_squares.append(square + [w])
        return


class Solution:
    def wordSquares(self, words: 'List[str]') -> 'List[List[str]]':
        if not words:
            return []
        all_squares = []
        square_l = len(words[0])
        if square_l == 1:
            return [words]
        t = buildTrie(words)
        for w in words:
            square = [w]
            possible_squares = []
            wordSquaresAux(square, [w[1]], t, square_l, possible_squares)
            if possible_squares:
                all_squares.extend(possible_squares)
        return all_squares
# @lc code=end
