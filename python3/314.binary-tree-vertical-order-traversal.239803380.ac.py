#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
#
# algorithms
# Medium (44.04%)
# Likes:    906
# Dislikes: 162
# Total Accepted:    108.2K
# Total Submissions: 245.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the vertical order traversal of its nodes'
# values. (ie, from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left to
# right.
# 
# Examples 1:
# 
# 
# Input: [3,9,20,null,null,15,7]
# 
# ⁠  3
# ⁠ /\
# ⁠/  \
# ⁠9  20
# ⁠   /\
# ⁠  /  \
# ⁠ 15   7 
# 
# Output:
# 
# [
# ⁠ [9],
# ⁠ [3,15],
# ⁠ [20],
# ⁠ [7]
# ]
# 
# 
# Examples 2:
# 
# 
# Input: [3,9,8,4,0,1,7]
# 
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠  9   8
# ⁠ /\  /\
# ⁠/  \/  \
# ⁠4  01   7 
# 
# Output:
# 
# [
# ⁠ [4],
# ⁠ [9],
# ⁠ [3,0,1],
# ⁠ [8],
# ⁠ [7]
# ]
# 
# 
# Examples 3:
# 
# 
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left
# child is 5)
# 
# ⁠    3
# ⁠   /\
# ⁠  /  \
# ⁠  9   8
# ⁠ /\  /\
# ⁠/  \/  \
# ⁠4  01   7
# ⁠   /\
# ⁠  /  \
# ⁠  5   2
# 
# Output:
# 
# [
# ⁠ [4],
# ⁠ [9,5],
# ⁠ [3,0,1],
# ⁠ [8,2],
# ⁠ [7]
# ]
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        columns = collections.defaultdict(list)
        bfs = collections.deque([(0, root)])
        min_col = 0
        while len(bfs):
            curr_col, curr_node = bfs.popleft()
            columns[curr_col].append(curr_node.val)
            if curr_node.left is not None:
                bfs.append((curr_col - 1, curr_node.left))
                min_col = min(min_col, curr_col - 1)
            if curr_node.right is not None:
                bfs.append((curr_col + 1, curr_node.right))
        vertical_order = []
        while min_col in columns:
            vertical_order.append(columns[min_col])
            del columns[min_col]
            min_col += 1
        return vertical_order
            
# @lc code=end
