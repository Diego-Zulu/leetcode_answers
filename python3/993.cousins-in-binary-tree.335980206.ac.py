#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#
# https://leetcode.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (52.14%)
# Likes:    736
# Dislikes: 45
# Total Accepted:    94.3K
# Total Submissions: 180.8K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# In a binary tree, the root node is at depth 0, and children of each depth k
# node are at depth k+1.
# 
# Two nodes of a binary tree are cousins if they have the same depth, but have
# different parents.
# 
# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree.
# 
# Return true if and only if the nodes corresponding to the values x and y are
# cousins.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if x == y or root is None:
            return False
        parents_bfs = defaultdict(lambda: None)
        bfs = deque([root])
        while bfs:
            if None not in [parents_bfs[x], parents_bfs[y]] and parents_bfs[x] != parents_bfs[y]:
                return True
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                parents_bfs.pop(curr.val, None)
                if curr.left:
                    bfs.append(curr.left)
                    parents_bfs[curr.left.val] = curr
                if curr.right:
                    bfs.append(curr.right)
                    parents_bfs[curr.right.val] = curr
        return False
# @lc code=end