#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#
# https://leetcode.com/problems/walls-and-gates/description/
#
# algorithms
# Medium (53.35%)
# Likes:    1050
# Dislikes: 15
# Total Accepted:    113.7K
# Total Submissions: 212.9K
# Testcase Example:  '[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]'
#
# You are given a m x n 2D grid initialized with these three possible
# values.
# 
# 
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to
# represent INF as you may assume that the distance to a gate is less than
# 2147483647.
# 
# 
# Fill each empty room with the distance to its nearest gate. If it is
# impossible to reach a gate, it should be filled with INF.
# 
# Example: 
# 
# Given the 2D grid:
# 
# 
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
# ⁠ 0  -1 INF INF
# 
# 
# After running your function, the 2D grid should be:
# 
# 
# ⁠ 3  -1   0   1
# ⁠ 2   2   1  -1
# ⁠ 1  -1   2  -1
# ⁠ 0  -1   3   4
# 
# 
#

# @lc code=start
def is_inside(r, c, rooms):
    return r >= 0 and c >= 0 and r < len(rooms) and c < len(rooms[0])

def dfs(queue, rooms):
    while queue:
        r, c, dist = queue.popleft()
        if not is_inside(r, c, rooms) or rooms[r][c] == -1 or rooms[r][c] <= dist:
            continue
        rooms[r][c] = dist
        queue.append((r+1, c, dist+1))
        queue.append((r, c+1, dist+1))
        queue.append((r-1, c, dist+1))
        queue.append((r, c-1, dist+1))
    

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    rooms[r][c] = 1
                    dfs(collections.deque([(r, c, 0)]), rooms)
                    rooms[r][c] = 0
                    
# @lc code=end
