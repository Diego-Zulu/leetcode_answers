#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (35.06%)
# Likes:    1058
# Dislikes: 2734
# Total Accepted:    545.4K
# Total Submissions: 1.6M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        filtered = list(filter(lambda x: x.isalnum(), s.lower()))
        l = len(filtered)
        middle = int(l / 2)
        after_middle = middle + (0 if l & 1 else -1)
        return filtered[:middle] == filtered[l-1:after_middle:-1]
# @lc code=end
