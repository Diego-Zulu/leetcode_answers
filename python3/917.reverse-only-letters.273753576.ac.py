#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (57.49%)
# Likes:    480
# Dislikes: 34
# Total Accepted:    51.5K
# Total Submissions: 89.5K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# 
# Example 2:
# 
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# 
# Example 3:
# 
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left = 0
        right = len(S) - 1
        R = list(S)
        while left < right:
            while left < right and not R[left].isalpha():
                left += 1
            while right > left and not R[right].isalpha():
                right -= 1
            R[left], R[right] = R[right], R[left]
            left += 1
            right -= 1
        return ''.join(R)
# @lc code=end
