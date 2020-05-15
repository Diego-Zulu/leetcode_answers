#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges/description/
#
# algorithms
# Medium (24.04%)
# Likes:    312
# Dislikes: 1772
# Total Accepted:    80.9K
# Total Submissions: 336.4K
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
# Given a sorted integer array nums, where the range of elements are in the
# inclusive range [lower, upper], return its missing ranges.
# 
# Example:
# 
# 
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
# 
# 
#

# @lc code=start
def try_append_result(ret, lower, upper):
     if upper > lower:
        rang = [str(lower)]
        if lower < upper - 1:
            rang.append(str(upper-1))
        ret.append('->'.join(rang))

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ret = []
        for n in nums:
            try_append_result(ret, lower, n)
            lower = n + 1
        try_append_result(ret, lower, upper + 1)
        return ret
# @lc code=end
