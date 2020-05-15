#
# @lc app=leetcode id=616 lang=python3
#
# [616] Add Bold Tag in String
#
# https://leetcode.com/problems/add-bold-tag-in-string/description/
#
# algorithms
# Medium (41.93%)
# Likes:    462
# Dislikes: 57
# Total Accepted:    32.9K
# Total Submissions: 78.4K
# Testcase Example:  '"abcxyz123"\n["abc","123"]'
#
# Given a string s and a list of strings dict, you need to add a closed pair of
# bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two
# such substrings overlap, you need to wrap them together by only one pair of
# closed bold tag. Also, if two substrings wrapped by bold tags are
# consecutive, you need to combine them.
# Example 1:
# 
# 
# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# 
# 
# 
# 
# Constraints:
# 
# 
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].
# 
# 
# Note: This question is the same as 758:
# https://leetcode.com/problems/bold-words-in-string/
# 
#

# @lc code=start
class Solution:
    def addBoldTag(self, s, dict_b):
        if not s or not dict_b:
            return s
        len_s = len(s)
        mask = [False] * (len_s + 1)
        for entry in dict_b:
            l = s.find(entry)
            while l > -1:
                mask[l:l+len(entry)] = [True] * (len(entry))
                l = s.find(entry, l+1)
        sol = []
        if mask[0]:
            sol.append("<b>")
        for i in range(len_s):
            sol.append(s[i])
            if mask[i] != mask[i + 1]:
                if mask[i]:
                    sol.append("</b>")
                else:
                    sol.append("<b>")
        return ''.join(sol)
# @lc code=end
