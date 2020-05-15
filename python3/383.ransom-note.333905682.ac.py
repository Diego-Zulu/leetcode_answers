#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (53.16%)
# Likes:    573
# Dislikes: 191
# Total Accepted:    210.1K
# Total Submissions: 395.6K
# Testcase Example:  '"a"\n"b"'
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return
# false.
# 
# Each letter in the magazine string can only be used once in your ransom
# note.
# 
# 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
# 
# Constraints:
# 
# 
# You may assume that both strings contain only lowercase letters.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)
        for l, c in ransom.items():
            if mag.get(l, 0) < c:
                return False
        return True
# @lc code=end
