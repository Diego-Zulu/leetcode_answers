#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (50.49%)
# Likes:    2033
# Dislikes: 154
# Total Accepted:    119.1K
# Total Submissions: 235.8K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
  '[2.0,3.0]\n' +
  '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# According to the example above:
# 
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#

# @lc code=start
from collections import defaultdict


def searchPath(visited, start, finish, graph):
    if start not in visited:
        visited[start] = -1.0
        start_connections = graph[start]
        if finish in start_connections:
            return start_connections[finish]
        for k,v in list(start_connections.items()):
            if v < 0:
                continue
            found_value = searchPath(visited, k, finish, graph)
            new_value = found_value * v
            if new_value >= 0:
                break
        if new_value < 0:
            new_value = -1.0
        graph[start][finish] = new_value
        visited[start] = new_value
        return new_value
    else:
        return visited[start]

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        evaluated = []
        for e, v in zip(equations, values):
            graph[e[0]][e[0]] = graph[e[1]][e[1]] = 1.0
            graph[e[0]][e[1]] = v
            graph[e[1]][e[0]] = 1 / v if v > 0 else 0
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                evaluated.append(-1.0)
            else:
                evaluated.append(searchPath(dict(), q[0], q[1], graph))
        return evaluated
# @lc code=end
