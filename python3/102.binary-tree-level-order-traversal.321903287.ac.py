#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (53.24%)
# Likes:    2645
# Dislikes: 65
# Total Accepted:    571.2K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        bfs = deque([root])
        while bfs:
            level_l = len(bfs)
            next_level = []
            for _ in range(level_l):
                curr = bfs.pop()
                if not curr:
                    continue
                next_level.append(curr.val)
                bfs.appendleft(curr.left)
                bfs.appendleft(curr.right)
            if next_level: 
                levels.append(next_level)
        return levels
        
# @lc code=end
