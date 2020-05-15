/*
 * @lc app=leetcode id=231 lang=java
 *
 * [231] Power of Two
 *
 * https://leetcode.com/problems/power-of-two/description/
 *
 * algorithms
 * Easy (42.97%)
 * Likes:    682
 * Dislikes: 168
 * Total Accepted:    287.2K
 * Total Submissions: 668.4K
 * Testcase Example:  '1'
 *
 * Given an integer, write a function to determine if it is a power of two.
 * 
 * Example 1:
 * 
 * 
 * Input: 1
 * Output: true 
 * Explanation: 2^0 = 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 16
 * Output: true
 * Explanation: 2^4 = 16
 * 
 * Example 3:
 * 
 * 
 * Input: 218
 * Output: false
 * 
 */

// @lc code=start
public class Solution {
    public boolean isPowerOfTwo(int n) {
        
        if (n <= 0) return false;
        while (n>1) {
            if (n%2 == 0) n = n/2;
            else return false;
        }
        
        return true;
    }
}
// @lc code=end
