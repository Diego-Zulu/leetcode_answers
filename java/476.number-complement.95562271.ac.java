/*
 * @lc app=leetcode id=476 lang=java
 *
 * [476] Number Complement
 *
 * https://leetcode.com/problems/number-complement/description/
 *
 * algorithms
 * Easy (64.71%)
 * Likes:    820
 * Dislikes: 81
 * Total Accepted:    181.2K
 * Total Submissions: 280.2K
 * Testcase Example:  '5'
 *
 * Given a positive integer num, output its complement number. The complement
 * strategy is to flip the bits of its binary representation.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: num = 5
 * Output: 2
 * Explanation: The binary representation of 5 is 101 (no leading zero bits),
 * and its complement is 010. So you need to output 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: num = 1
 * Output: 0
 * Explanation: The binary representation of 1 is 1 (no leading zero bits), and
 * its complement is 0. So you need to output 0.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The given integer num is guaranteed to fit within the range of a 32-bit
 * signed integer.
 * num >= 1
 * You could assume no leading zero bit in the integer’s binary
 * representation.
 * This question is the same as 1009:
 * https://leetcode.com/problems/complement-of-base-10-integer/
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int findComplement(int num) {
        
        int complement = 0;
        int aux = 0;
        
        for (int i=0; i<32; i++) {
            
            aux |= 1<<i;
            if (aux >= num) {
                complement = num ^ aux;
                break;
            }
        }
        
        return complement;
    }
}
// @lc code=end
