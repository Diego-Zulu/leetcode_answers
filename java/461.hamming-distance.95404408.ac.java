/*
 * @lc app=leetcode id=461 lang=java
 *
 * [461] Hamming Distance
 *
 * https://leetcode.com/problems/hamming-distance/description/
 *
 * algorithms
 * Easy (71.50%)
 * Likes:    1611
 * Dislikes: 153
 * Total Accepted:    297.7K
 * Total Submissions: 416.2K
 * Testcase Example:  '1\n4'
 *
 * The Hamming distance between two integers is the number of positions at
 * which the corresponding bits are different.
 * 
 * Given two integers x and y, calculate the Hamming distance.
 * 
 * Note:
 * 0 ≤ x, y < 2^31.
 * 
 * 
 * Example:
 * 
 * Input: x = 1, y = 4
 * 
 * Output: 2
 * 
 * Explanation:
 * 1   (0 0 0 1)
 * 4   (0 1 0 0)
 * ⁠      ↑   ↑
 * 
 * The above arrows point to positions where the corresponding bits are
 * different.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int hammingDistance(int x, int y) {
        
        int dif = x ^ y;
        
        int result = 0;

        for (int i = 0; dif > 0; i=1) {

            dif = (dif >> i);

            if ((dif & 1) > 0) {
                result++;
            }
        }
        
        return result;
    }
}
// @lc code=end
