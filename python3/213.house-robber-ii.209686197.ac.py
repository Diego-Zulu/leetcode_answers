#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (36.12%)
# Likes:    1526
# Dislikes: 46
# Total Accepted:    162K
# Total Submissions: 448.4K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        len_n = len(nums)
        if len_n <= 2: return max(nums, default=0)
        return max(robAux(0, len_n - 1, nums), robAux(1, len_n, nums))
    
def robAux(pos: 'int', till: 'int',  nums: 'List[int]') -> 'int':
    robbed = [[0, 0] for i in range(till + 1)] 
    for i in range(1 + pos, till + 1):
        robbed[i][0] = max(robbed[i-1][0], robbed[i-1][1])
        robbed[i][1] = robbed[i-1][0] + nums[i-1]
    return max(robbed[till])
# @lc code=end
