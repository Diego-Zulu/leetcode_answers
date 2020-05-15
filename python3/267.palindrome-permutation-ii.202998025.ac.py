#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#
# https://leetcode.com/problems/palindrome-permutation-ii/description/
#
# algorithms
# Medium (35.80%)
# Likes:    397
# Dislikes: 51
# Total Accepted:    35.6K
# Total Submissions: 99.4K
# Testcase Example:  '"aabb"'
#
# Given a string s, return all the palindromic permutations (without
# duplicates) of it. Return an empty list if no palindromic permutation could
# be form.
# 
# Example 1:
# 
# 
# Input: "aabb"
# Output: ["abba", "baab"]
# 
# Example 2:
# 
# 
# Input: "abc"
# Output: []
# 
#

# @lc code=start
from collections import Counter

def genPalindromesAux(current_word, count, odd_len, ret):
    added_letter = False
    for k, v in count.items():
        if v > 0:
            current_word.append(k)
            count[k] -= 2
            genPalindromesAux(current_word, count, odd_len, ret)
            current_word.pop()
            count[k] += 2
            added_letter = True
    if not added_letter:
        if odd_len:
            current_word = current_word[-1:-len(current_word):-1] + current_word
        else:
            current_word = current_word[-1:-len(current_word) - 1:-1] + current_word
        ret.append(''.join(current_word))

class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 0: 
            return []
        count = Counter(s)
        odd_count = 0
        starting_letter = None
        for k, v in count.items():
            if v % 2:
                odd_count += 1
                starting_letter = k
            elif starting_letter is None:
                starting_letter = k
        if odd_count > 1 or (odd_count == 1 and len(s) % 2 == 0) or (odd_count == 0 and len(s) % 2):
            return []
        
        ret = []
        starting_word = []
        if len(s) % 2:
            count[starting_letter] -= 1
            starting_word.append(starting_letter)
        genPalindromesAux(starting_word, count, len(s) % 2, ret)
        
        return ret
        
# @lc code=end
