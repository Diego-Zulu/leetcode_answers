/*
 * @lc app=leetcode id=268 lang=java
 *
 * [268] Missing Number
 *
 * https://leetcode.com/problems/missing-number/description/
 *
 * algorithms
 * Easy (50.89%)
 * Likes:    1569
 * Dislikes: 1932
 * Total Accepted:    422K
 * Total Submissions: 828.9K
 * Testcase Example:  '[3,0,1]'
 *
 * Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
 * find the one that is missing from the array.
 * 
 * Example 1:
 * 
 * 
 * Input: [3,0,1]
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [9,6,4,2,3,5,7,0,1]
 * Output: 8
 * 
 * 
 * Note:
 * Your algorithm should run in linear runtime complexity. Could you implement
 * it using only constant extra space complexity?
 */

// @lc code=start
public class Solution {
    public int missingNumber(int[] nums) {
        
        int totalSum = nums.length;
        int numsSum = 0;
        
        for (int i=0; i<nums.length; i++) {
            
            totalSum += i;
            numsSum += nums[i];
        }
        
        return Math.abs(totalSum-numsSum);
    }
}
// @lc code=end
