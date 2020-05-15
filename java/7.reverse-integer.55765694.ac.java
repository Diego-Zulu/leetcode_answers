/*
 * @lc app=leetcode id=7 lang=java
 *
 * [7] Reverse Integer
 *
 * https://leetcode.com/problems/reverse-integer/description/
 *
 * algorithms
 * Easy (25.68%)
 * Likes:    3153
 * Dislikes: 4960
 * Total Accepted:    1.1M
 * Total Submissions: 4.1M
 * Testcase Example:  '123'
 *
 * Given a 32-bit signed integer, reverse digits of an integer.
 * 
 * Example 1:
 * 
 * 
 * Input: 123
 * Output: 321
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: -123
 * Output: -321
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 120
 * Output: 21
 * 
 * 
 * Note:
 * Assume we are dealing with an environment which could only store integers
 * within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
 * of this problem, assume that your function returns 0 when the reversed
 * integer overflows.
 * 
 */

// @lc code=start
public class Solution {
    public int reverse(int x) {
        
        int result = 0;
        int lastResult = 0;
        
        while (x != 0) {
            
            lastResult = result;
            result = result * 10 + x%10;
            if ((result - x%10) / 10 != lastResult) return 0;
            x /= 10;
        }
        
        return result;
    }
}
// @lc code=end
