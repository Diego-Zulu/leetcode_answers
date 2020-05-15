#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (46.13%)
# Likes:    1764
# Dislikes: 91
# Total Accepted:    333.1K
# Total Submissions: 721.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        bfs = deque([root])
        reverse = False
        while bfs:
            level_l = len(bfs)
            next_level = deque()
            for _ in range(level_l):
                curr = bfs.pop()
                if not curr:
                    continue
                if reverse:
                    next_level.appendleft(curr.val)
                else:
                    next_level.append(curr.val)
                bfs.appendleft(curr.left)
                bfs.appendleft(curr.right)
            reverse = not reverse
            if next_level: 
                levels.append(next_level)
        return levels
# @lc code=end
