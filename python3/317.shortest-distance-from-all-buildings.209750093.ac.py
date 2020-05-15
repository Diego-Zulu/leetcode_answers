#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#
# https://leetcode.com/problems/shortest-distance-from-all-buildings/description/
#
# algorithms
# Hard (40.84%)
# Likes:    732
# Dislikes: 42
# Total Accepted:    63.9K
# Total Submissions: 156.4K
# Testcase Example:  '[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# You want to build a house on an empty land which reaches all buildings in the
# shortest amount of distance. You can only move up, down, left and right. You
# are given a 2D grid of values 0, 1 or 2, where:
# 
# 
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# 
# 
# Example:
# 
# 
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# 
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 
# Output: 7 
# 
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at
# (0,2),
# ⁠            the point (1,2) is an ideal empty land to build a house, as the
# total 
# travel distance of 3+3+1=7 is minimal. So return 7.
# 
# Note:
# There will be at least one building. If it is not possible to build such
# house according to the above rules, return -1.
# 
#

# @lc code=start
def bfs(next_pos, grid):
    visited = set()
    houses_reached = 0
    while next_pos:
        r, c, steps = next_pos.popleft()
        curr_steps, paths = grid[r][c]
        if paths <= -1:
            if paths == -1:
                houses_reached += 1
            continue
        elif (r, c) in visited:
            continue
        visited.add((r, c))
        grid[r][c] = (curr_steps + steps, paths + 1)
        steps += 1
        next_pos.append((r-1, c, steps))
        next_pos.append((r, c-1, steps))
        next_pos.append((r+1, c, steps))
        next_pos.append((r, c+1, steps))
    return houses_reached
    

class Solution:
    def shortestDistance(self, grid_og: 'List[List[int]]') -> 'int':
        n = len(grid_og)
        m = len(grid_og[0])
        houses = []
        max_val = n*m*n*m + 1
        grid = [[(max_val, -2) for i in range(m + 2)]]
        for r in range(n):
            row = []
            row.append((max_val, -2))
            for c in range(m):
                pos_val = (max_val, -2)
                if grid_og[r][c] == 1:
                    houses.append((r+1, c+1))  
                    pos_val = (max_val, -1)
                elif grid_og[r][c] == 0:
                    pos_val = (0, 0)
                row.append(pos_val)
            row.append((max_val, -2))
            grid.append(row)
        grid.append([(max_val, -2) for i in range(m + 2)])
        houses_num = len(houses)
        for house in houses:
            initial_queue = collections.deque([
                (house[0]-1, house[1], 1),
                (house[0], house[1]-1, 1),
                (house[0]+1, house[1], 1),
                (house[0], house[1]+1, 1),
            ])
            if houses_num > bfs(initial_queue, grid):
                return -1
        min_dist = max_val
        for r in range(1, n+1):
            for c in range(1, m+1):
                steps, paths = grid[r][c]
                if paths == houses_num:
                    min_dist = min(min_dist, steps)
        return min_dist
# @lc code=end
