#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#
# https://leetcode.com/problems/minimum-area-rectangle/description/
#
# algorithms
# Medium (52.14%)
# Likes:    575
# Dislikes: 113
# Total Accepted:    43.7K
# Total Submissions: 83.8K
# Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
#
# Given a set of points in the xy-plane, determine the minimum area of a
# rectangle formed from these points, with sides parallel to the x and y axes.
# 
# If there isn't any rectangle, return 0.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
import sys

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        found_x = {}
        ans = sys.maxsize
        for x, columns_pos in sorted(columns.items(), key= lambda x: x[0]):
            columns_pos.sort()
            for i, y2 in enumerate(columns_pos):
                for j in range(i):
                    y1 = columns_pos[j]
                    if (y1, y2) in found_x:
                        ans = min(ans, (x - found_x[y1, y2]) * (y2 - y1))
                    found_x[y1, y2] = x
        return 0 if sys.maxsize == ans else ans
                    
# @lc code=end
