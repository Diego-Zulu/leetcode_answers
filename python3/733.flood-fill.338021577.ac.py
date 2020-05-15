#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (54.73%)
# Likes:    1044
# Dislikes: 185
# Total Accepted:    149.7K
# Total Submissions: 273.9K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# 
# An image is represented by a 2-D array of integers, each integer representing
# the pixel value of the image (from 0 to 65535).
# 
# Given a coordinate (sr, sc) representing the starting pixel (row and column)
# of the flood fill, and a pixel value newColor, "flood fill" the image.
# 
# To perform a "flood fill", consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color as the starting pixel), and so on.  Replace the
# color of all of the aforementioned pixels with the newColor.
# 
# At the end, return the modified image.
# 
# Example 1:
# 
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels
# connected 
# by a path of the same color as the starting pixel are colored with the new
# color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected
# to the starting pixel.
# 
# 
# 
# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0  and 0 .
# The value of each color in image[i][j] and newColor will be an integer in [0,
# 65535].
# 
#

# @lc code=start
def outside(r, c, image):
    return r < 0 or c < 0 or r >= len(image) or c >= len(image[0])

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        bfs = collections.deque([(sr, sc)])
        initialColor = image[sr][sc]
        if newColor == initialColor:
            return image
        while bfs:
            curr_r, curr_c = bfs.popleft()
            if outside(curr_r, curr_c, image) or initialColor != image[curr_r][curr_c]:
                continue
            image[curr_r][curr_c] = newColor
            for sum_r, sum_c in [(1, 0), (0, 1)]:
                bfs.append((curr_r + sum_r, curr_c + sum_c))
                bfs.append((curr_r - sum_r, curr_c - sum_c))
        return image
        
# @lc code=end
