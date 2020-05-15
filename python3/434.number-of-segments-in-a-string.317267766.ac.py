#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (37.54%)
# Likes:    198
# Dislikes: 699
# Total Accepted:    73.1K
# Total Submissions: 194.6K
# Testcase Example:  '"Hello, my name is John"'
#
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
# 
# Please note that the string does not contain any non-printable characters.
# 
# Example:
# 
# Input: "Hello, my name is John"
# Output: 5
# 
# 
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
# @lc code=end
