/*
 * @lc app=leetcode id=485 lang=java
 *
 * [485] Max Consecutive Ones
 *
 * https://leetcode.com/problems/max-consecutive-ones/description/
 *
 * algorithms
 * Easy (55.74%)
 * Likes:    573
 * Dislikes: 349
 * Total Accepted:    200.8K
 * Total Submissions: 360.6K
 * Testcase Example:  '[1,0,1,1,0,1]'
 *
 * Given a binary array, find the maximum number of consecutive 1s in this
 * array.
 * 
 * Example 1:
 * 
 * Input: [1,1,0,1,1,1]
 * Output: 3
 * Explanation: The first two digits or the last three digits are consecutive
 * 1s.
 * ⁠   The maximum number of consecutive 1s is 3.
 * 
 * 
 * 
 * Note:
 * 
 * The input array will only contain 0 and 1.
 * The length of input array is a positive integer and will not exceed 10,000
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
        int result = 0;
        int actualLength = 0;
        
        for (int i=0; i<nums.length; i++) {
            
            if (nums[i] == 1) {
                actualLength++;
                if (actualLength > result) {
                    result = actualLength;
                }
            } else {
                actualLength = 0;
            }
        }
        
        return actualLength > result ? actualLength : result;
    }
}
// @lc code=end
