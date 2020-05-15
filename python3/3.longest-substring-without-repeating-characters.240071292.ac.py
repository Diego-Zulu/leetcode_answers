#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.94%)
# Likes:    8656
# Dislikes: 525
# Total Accepted:    1.5M
# Total Submissions: 4.9M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_present = set()
        left, longest = 0, 0
        "tmmzuxt"
        for right, c in enumerate(s):
            if c in chars_present:
                longest = max(longest, right - left)
                while left < right and s[left] != c:
                    chars_present.remove(s[left])
                    left += 1
                left += 1
            chars_present.add(c)
        return max(longest, len(s) - left)
            
# @lc code=end
