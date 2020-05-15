#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (74.17%)
# Likes:    654
# Dislikes: 56
# Total Accepted:    50.5K
# Total Submissions: 68.1K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
# 
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
# 
# 
# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Note:
# 
# 
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
# 
#

# @lc code=start
def dfs(graph, curr_path, paths):
    if curr_path[-1] == len(graph) - 1:
        paths.append(list(curr_path))
        return
    for n in graph[curr_path[-1]]:
        curr_path.append(n)
        dfs(graph, curr_path, paths)
        curr_path.pop()
        
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        dfs(graph, [0], paths)
        return paths
# @lc code=end
