#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (50.64%)
# Likes:    739
# Dislikes: 69
# Total Accepted:    94.4K
# Total Submissions: 186.4K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. You may
# assume that each word will contain only lower case letters. If no such two
# words exist, return 0.
# 
# Example 1:
# 
# 
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".
# 
# Example 2:
# 
# 
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4 
# Explanation: The two words can be "ab", "cd".
# 
# Example 3:
# 
# 
# Input: ["a","aa","aaa","aaaa"]
# Output: 0 
# Explanation: No such pair of words.
# 
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, words: 'List[str]') -> 'int':
        present_letters_for_words = []
        for w in words:
            letters = 0
            for c in w:
                letters |= 1 << (ord(c) - ord('a'))
            present_letters_for_words.append((letters, len(w)))
        max_prod = 0
        for i in range(len(words) - 1):
            w1 = present_letters_for_words[i]
            for j in range(i+1, len(words)):
                w2 = present_letters_for_words[j]
                if (w1[0] & w2[0]) == 0:
                    max_prod = max(max_prod, w1[1] * w2[1])
        return max_prod
# @lc code=end
