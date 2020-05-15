#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (47.69%)
# Likes:    6376
# Dislikes: 111
# Total Accepted:    476.5K
# Total Submissions: 998.8K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l: int = 0
        r: int = len(height) - 1
        l_max: int = 0
        r_max: int = len(height) - 1
        water: int = 0
        while l < r:
            if height[l] < height[r]:
                if height[l_max] <= height[l]:
                    l_max = l
                else:
                    water += height[l_max] - height[l]
                l += 1
            else:
                if height[r_max] <= height[r]:
                    r_max = r
                else:
                    water += height[r_max] - height[r]
                r -= 1
                
        return water
# @lc code=end
