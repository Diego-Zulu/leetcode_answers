#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#
# https://leetcode.com/problems/distant-barcodes/description/
#
# algorithms
# Medium (41.54%)
# Likes:    282
# Dislikes: 16
# Total Accepted:    13K
# Total Submissions: 31.2K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# In a warehouse, there is a row of barcodes, where the i-th barcode is
# barcodes[i].
# 
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
# return any answer, and it is guaranteed an answer exists.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcodes_count = collections.Counter(barcodes)
        barcodes_queue, ordered_barcodes, N = [], [], len(barcodes)
        for k, v in barcodes_count.items():
            heapq.heappush(barcodes_queue, (-v, k))
        while len(ordered_barcodes) < N:
            available, barcode = heapq.heappop(barcodes_queue)
            if len(ordered_barcodes) > 0 and ordered_barcodes[-1] == barcode:
                next_available, next_barcode = heapq.heappop(barcodes_queue)
                heapq.heappush(barcodes_queue, (next_available+1, next_barcode))
                ordered_barcodes.append(next_barcode)
            ordered_barcodes.append(barcode)
            heapq.heappush(barcodes_queue, (available+1, barcode))
        return ordered_barcodes
        
# @lc code=end
