#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#
# https://leetcode.com/problems/palindrome-permutation/description/
#
# algorithms
# Easy (61.47%)
# Likes:    336
# Dislikes: 51
# Total Accepted:    86.4K
# Total Submissions: 140.6K
# Testcase Example:  '"code"'
#
# Given a string, determine if a permutation of the string could form a
# palindrome.
# 
# Example 1:
# 
# 
# Input: "code"
# Output: false
# 
# Example 2:
# 
# 
# Input: "aab"
# Output: true
# 
# Example 3:
# 
# 
# Input: "carerac"
# Output: true
# 
#

# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        number_of_letters = collections.Counter(s)
        num_odd = 0
        for i in number_of_letters.values():
            if i & 1:
                num_odd += 1
                if num_odd == 2:
                    return False
        return True
# @lc code=end
