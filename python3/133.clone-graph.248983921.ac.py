#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (32.94%)
# Likes:    1542
# Dislikes: 1293
# Total Accepted:    315.5K
# Total Submissions: 955.5K
# Testcase Example:  '[[2,4],[1,3],[2,4],[1,3]]'
#
# Given a reference of a node in a connected undirected graph.
# 
# Return a deep copy (clone) of the graph.
# 
# Each node in the graph contains a val (int) and a list (List[Node]) of its
# neighbors.
# 
# 
# class Node {
# ⁠   public int val;
# ⁠   public List<Node> neighbors;
# }
# 
# 
# 
# 
# Test case format:
# 
# For simplicity sake, each node's value is the same as the node's index
# (1-indexed). For example, the first node with val = 1, the second node with
# val = 2, and so on. The graph is represented in the test case using an
# adjacency list.
# 
# Adjacency list is a collection of unordered lists used to represent a finite
# graph. Each list describes the set of neighbors of a node in the graph.
# 
# The given node will always be the first node with val = 1. You must return
# the copy of the given node as a reference to the cloned graph.
# 
# 
# Example 1:
# 
# 
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val =
# 3).
# 
# 
# Example 2:
# 
# 
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists
# of only one node with val = 1 and it does not have any neighbors.
# 
# 
# Example 3:
# 
# 
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
# 
# 
# Example 4:
# 
# 
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# Number of Nodes will not exceed 100.
# There is no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given
# node.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

def create_new_nodes(node, og_to_clone):
    if node in og_to_clone:
        return
    og_to_clone[node] = Node(node.val, node.neighbors)
    for n in node.neighbors:
        create_new_nodes(n, og_to_clone)
    
def link_new_nodes(new_node, og_to_clone, visited):
    if new_node in visited:
        return
    new_node.neighbors = [og_to_clone[n] for n in new_node.neighbors]
    visited.add(new_node)
    for n in new_node.neighbors:
        link_new_nodes(n, og_to_clone, visited)

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        og_to_clone = {}
        create_new_nodes(node, og_to_clone)
        ret_node = og_to_clone[node]
        link_new_nodes(ret_node, og_to_clone, set())
        return ret_node
# @lc code=end
