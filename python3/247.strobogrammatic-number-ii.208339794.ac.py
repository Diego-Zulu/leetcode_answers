#
# @lc app=leetcode id=247 lang=python3
#
# [247] Strobogrammatic Number II
#
# https://leetcode.com/problems/strobogrammatic-number-ii/description/
#
# algorithms
# Medium (46.99%)
# Likes:    400
# Dislikes: 117
# Total Accepted:    71K
# Total Submissions: 151K
# Testcase Example:  '2'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Find all strobogrammatic numbers that are of length = n.
# 
# Example:
# 
# 
# Input:  n = 2
# Output: ["11","69","88","96"]
# 
# 
#

# @lc code=start
class Solution:
    def findStrobogrammatic(self, n: 'int') -> 'List[str]':
        even = ["11","69","88","96", "00"]
        odd = ["0", "1", "8"]
        if n == 1:
            return odd
        elif n == 2:
            return even[:len(even)-1]
        elif n & 1:
            last_solution, candidate = self.findStrobogrammatic(n-1), odd
        else:
            last_solution, candidate = self.findStrobogrammatic(n-2), even
        middle = int((n-1)/2)
        return [l[:middle] + c + l[middle:] for c in candidate for l in last_solution]
# @lc code=end
