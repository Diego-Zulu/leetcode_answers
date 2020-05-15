#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#
# https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
#
# algorithms
# Medium (42.22%)
# Likes:    417
# Dislikes: 96
# Total Accepted:    83.6K
# Total Submissions: 197.9K
# Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
#
# Given an input string , reverse the string word by word. 
# 
# Example:
# 
# 
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# 
# Note: 
# 
# 
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# 
# 
# Follow up: Could you do it in-place without allocating extra space?
# 
#

# @lc code=start
def reverse(s, start, end):
    l = start
    r = end - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        start = 0
        end = 0
        while end < len(s):
            if s[end] == ' ':
                reverse(s, start, end)
                start = end + 1
            end += 1
        reverse(s, start, end)
# @lc code=end
