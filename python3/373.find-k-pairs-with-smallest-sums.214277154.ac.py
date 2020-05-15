#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (35.94%)
# Likes:    1212
# Dislikes: 94
# Total Accepted:    94.7K
# Total Submissions: 263.5K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# You are given two integer arrays nums1 and nums2 sorted in ascending order
# and an integer k.
# 
# Define a pair (u,v) which consists of one element from the first array and
# one element from the second array.
# 
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]] 
# Explanation: The first 3 pairs are returned from the sequence: 
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# Example 2:
# 
# 
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence: 
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# Example 3:
# 
# 
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
# 
# 
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        n, m = len(nums1), len(nums2)
        if n*m == 0:
            return []
        k = min(k, n*m)
        visited = set([(0,0)])
        smallest = []
        heapq.heappush(smallest, (nums1[0] + nums2[0], (0, 0)))
        smallest_k_pairs = []
        while k > 0:
            k -= 1
            smallest_k = heapq.heappop(smallest)
            pos = smallest_k[1]
            smallest_k_pairs.append([nums1[pos[0]], nums2[pos[1]]])
            if pos[1] + 1 < m and (pos[0], pos[1]+1) not in visited:
                visited.add((pos[0], pos[1]+1))
                heapq.heappush(smallest, (nums1[pos[0]] + nums2[pos[1]+1], (pos[0], pos[1]+1)))
            if pos[0] + 1 < n and (pos[0]+1, pos[1]) not in visited:
                visited.add((pos[0]+1, pos[1]))
                heapq.heappush(smallest, (nums1[pos[0]+1] + nums2[pos[1]], (pos[0]+1, pos[1])))
        return smallest_k_pairs
# @lc code=end
