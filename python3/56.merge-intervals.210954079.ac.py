#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (38.53%)
# Likes:    3728
# Dislikes: 270
# Total Accepted:    556.1K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals: return []
        intervals = collections.deque(sorted(intervals, key= lambda x: x.start))
        result = []
        while len(intervals) > 1:
            l = intervals.popleft()
            r = intervals.popleft()
            if l.end >= r.start:
                r = Interval(l.start, max(r.end, l.end))
            else:
                result.append(l)
            intervals.appendleft(r)
        result.append(intervals.pop())
        return result
# @lc code=end
