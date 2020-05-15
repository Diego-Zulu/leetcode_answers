#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#
# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
#
# algorithms
# Easy (48.76%)
# Likes:    306
# Dislikes: 46
# Total Accepted:    70.1K
# Total Submissions: 143.7K
# Testcase Example:  '[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]'
#
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
# represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.
# 
# 
#

# @lc code=start
def belongs_in_line(point1, m, other):
    if m is None:
        return other[0] == point1[0]
    left = other[1] - point1[1]
    right = m * (other[0] - point1[0])
    return left == right

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        point1, point2 = coordinates[:2]
        m = None
        if point1[0] != point2[0]:
            m = (point1[1] - point2[1]) / (point1[0] - point2[0])
        return all(map(lambda x: belongs_in_line(point1, m, x), coordinates))
# @lc code=end
