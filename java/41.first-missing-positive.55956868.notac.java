/*
 * @lc app=leetcode id=41 lang=java
 *
 * [41] First Missing Positive
 *
 * https://leetcode.com/problems/first-missing-positive/description/
 *
 * algorithms
 * Hard (31.27%)
 * Likes:    3107
 * Dislikes: 754
 * Total Accepted:    313.3K
 * Total Submissions: 1M
 * Testcase Example:  '[1,2,0]'
 *
 * Given an unsorted integer array, find the smallest missing positive
 * integer.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,0]
 * Output: 3
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [3,4,-1,1]
 * Output: 2
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [7,8,9,11,12]
 * Output: 1
 * 
 * 
 * Note:
 * 
 * Your algorithm should run in O(n) time and uses constant extra space.
 * 
 */

// @lc code=start
public class Solution {
    public int firstMissingPositive(int[] nums) {
        
        if (nums.length < 1) return 1;
        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int partialSum = 0;
        int totalSum = 0;
        
        for (int i=0; i<nums.length; i++) {
            if (nums[i] >= 0) {
                partialSum += nums[i];
                if (nums[i] < min) min = nums[i];
                if (nums[i] > max) max = nums[i];
            }
        }
        
        for (int i=min; i<max+1; i++) {
            
            totalSum += i;
        }
        
        if (partialSum == totalSum) {
            
            if (min > 1) return 1;
            else return max + 1;
            
        } else {
            
            return totalSum - partialSum;
        }
        
    }
}
// @lc code=end
