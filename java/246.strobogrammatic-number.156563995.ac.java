/*
 * @lc app=leetcode id=246 lang=java
 *
 * [246] Strobogrammatic Number
 *
 * https://leetcode.com/problems/strobogrammatic-number/description/
 *
 * algorithms
 * Easy (44.58%)
 * Likes:    199
 * Dislikes: 438
 * Total Accepted:    73.5K
 * Total Submissions: 164.7K
 * Testcase Example:  '"69"'
 *
 * A strobogrammatic number is a number that looks the same when rotated 180
 * degrees (looked at upside down).
 * 
 * Write a function to determine if a number is strobogrammatic. The number is
 * represented as a string.
 * 
 * Example 1:
 * 
 * 
 * Input:  "69"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input:  "88"
 * Output: true
 * 
 * Example 3:
 * 
 * 
 * Input:  "962"
 * Output: false
 * 
 */

// @lc code=start
class Solution {
    
    private static final char[] strobogrammaticNums = {'0', '1', '-', '-', '-', '-', '9', '-', '8', '6'};
    
    public boolean isStrobogrammatic(String num) {
        
        int left = 0;
        int right = num.length() - 1;
        
        while (left <= right) {
            int leftCharToPos = num.charAt(left) - '0';
            if (strobogrammaticNums[leftCharToPos] != num.charAt(right))
                return false;
            left++;
            right--;
        }
        
        return true;
    }
}
// @lc code=end
