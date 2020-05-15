#
# @lc app=leetcode id=685 lang=python
#
# [685] Redundant Connection II
#
# https://leetcode.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (32.20%)
# Likes:    685
# Dislikes: 198
# Total Accepted:    32.8K
# Total Submissions: 101.7K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 
# In this problem, a rooted tree is a directed graph such that, there is
# exactly one node (the root) for which all other nodes are descendants of this
# node, plus every node has exactly one parent, except for the root node which
# has no parents.
# 
# The given input is a directed graph that started as a rooted tree with N
# nodes (with distinct values 1, 2, ..., N), with one additional directed edge
# added.  The added edge has two different vertices chosen from 1 to N, and was
# not an edge that already existed.
# 
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] that represents a directed edge connecting nodes u and v,
# where u is a parent of child v.
# 
# Return an edge that can be removed so that the resulting graph is a rooted
# tree of N nodes.  If there are multiple answers, return the answer that
# occurs last in the given 2D-array.
# Example 1:
# 
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
# 
# 
# Example 2:
# 
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5  2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4 
# 
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
# 
#

# @lc code=start
def find(parents, child):
    while child != parents[child]:
        parents[child] = parents[parents[child]]
        child = parents[child]
    return child

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        cand1, cand2 = None, None
        parents = [i for i in range(len(edges) + 2)]
        for e in edges:
            if parents[e[1]] == e[1]:
                parents[e[1]] = e[0]
            else:
                cand1 = [parents[e[1]],e[1]]
                cand2 = [e[0], e[1]]
                e[1] = 0
        parents = [i for i in range(len(edges) + 2)]
        for e in edges:
            if e[1] == 0:
                continue
            if find(parents, e[0]) == e[1]:
                return cand1 if cand1 else e
            parents[e[1]] = e[0]
        return cand2
        
# @lc code=end
