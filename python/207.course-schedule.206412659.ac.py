#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (41.50%)
# Likes:    3262
# Dislikes: 167
# Total Accepted:    360.9K
# Total Submissions: 869K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input
# prerequisites.
# 1 <= numCourses <= 10^5
# 
# 
#

# @lc code=start
def foundCycle(grey, black, graph, i):
    grey.add(i)
    for g in graph[i]:
        if g in grey or (g not in black and foundCycle(grey, black, graph, g)):
            return True
    black.add(i)
    grey.remove(i)
    return False

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        black = set()
        grey = set()
        for p in prerequisites:
            graph[p[1]].append(p[0])
        for i in range(numCourses):
            if i not in black and foundCycle(grey, black, graph, i):
                return False
        return True
# @lc code=end
