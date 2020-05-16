#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (30.87%)
# Likes:    815
# Dislikes: 154
# Total Accepted:    125.7K
# Total Submissions: 406.8K
# Testcase Example:  '[1,0,2]'
#
# There are N children standing in a line. Each child is assigned a rating
# value.
# 
# You are giving candies to these children subjected to the following
# requirements:
# 
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# 
# 
# What is the minimum candies you must give?
# 
# Example 1:
# 
# 
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# ⁠            The third child gets 1 candy because it satisfies the above two
# conditions.
# 
# 
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        last_max_pos = -1
        last_max_candies = -1
        candies = 0
        last_candy_gave = 0
        for i, r in enumerate(ratings):
            last_rating = ratings[i-1] if i > 0 else -1
            candy_to_give = last_candy_gave

            if r > last_rating:
                candy_to_give += 1
            else:
                candy_to_give = 1
                
            if r < last_rating and last_candy_gave == candy_to_give:
                diff = i - last_max_pos
                candies += diff
                if diff < last_max_candies:
                    candies -= 1

            candies += candy_to_give
            last_candy_gave = candy_to_give
            if r >= last_rating:
                last_max_pos = i
                last_max_candies = candy_to_give
        return candies


# @lc code=end
