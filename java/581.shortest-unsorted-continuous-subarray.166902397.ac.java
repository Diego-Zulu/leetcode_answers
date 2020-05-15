/*
 * @lc app=leetcode id=581 lang=java
 *
 * [581] Shortest Unsorted Continuous Subarray
 *
 * https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
 *
 * algorithms
 * Easy (30.83%)
 * Likes:    2381
 * Dislikes: 121
 * Total Accepted:    112.1K
 * Total Submissions: 363.4K
 * Testcase Example:  '[2,6,4,8,10,9,15]'
 *
 * Given an integer array, you need to find one continuous subarray that if you
 * only sort this subarray in ascending order, then the whole array will be
 * sorted in ascending order, too.  
 * 
 * You need to find the shortest such subarray and output its length.
 * 
 * Example 1:
 * 
 * Input: [2, 6, 4, 8, 10, 9, 15]
 * Output: 5
 * Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make
 * the whole array sorted in ascending order.
 * 
 * 
 * 
 * Note:
 * 
 * Then length of the input array is in range [1, 10,000].
 * The input array may contain duplicates, so ascending order here means . 
 * 
 * 
 */

// @lc code=start
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        
        int sortStart = -1;
        int sortEnd = -1;
        int biggestInSort = Integer.MIN_VALUE;
        int smallestInSort = Integer.MAX_VALUE;
        
        for (int i=0; i<nums.length - 1; i++) {
            if ((sortEnd != i && nums[i] > nums[i+1]) || (sortEnd == i && biggestInSort > nums[i+1])) {
                
                if (sortStart == -1) {
                    sortStart = i;
                }
                if (smallestInSort > nums[i+1]) {
                    sortStart = moveLeftUntilSmaller(sortStart, nums[i+1], nums);
                    smallestInSort = nums[i+1];
                }
                sortEnd = i+1;
                biggestInSort = Math.max(nums[i], biggestInSort);
            }
        }
        
        if (sortStart == -1 || sortEnd == -1) return 0;
        
        return sortEnd - sortStart + 1;
    }
    
    private int moveLeftUntilSmaller(int sortStart, int numb, int[] nums) {
        
        for (int i=sortStart - 1; i>=0; i--) {
            
            if (numb >= nums[i]) {
                return i+1;
            }
        }
        
        return 0;
    }
}
// @lc code=end
