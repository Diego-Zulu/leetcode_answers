/*
 * @lc app=leetcode id=970 lang=java
 *
 * [970] Powerful Integers
 *
 * https://leetcode.com/problems/powerful-integers/description/
 *
 * algorithms
 * Easy (39.73%)
 * Likes:    123
 * Dislikes: 250
 * Total Accepted:    19.8K
 * Total Submissions: 49.9K
 * Testcase Example:  '2\n3\n10'
 *
 * Given two positive integers x and y, an integer is powerful if it is equal
 * to x^i + y^j for some integers i >= 0 and j >= 0.
 * 
 * Return a list of all powerful integers that have value less than or equal to
 * bound.
 * 
 * You may return the answer in any order.  In your answer, each value should
 * occur at most once.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: x = 2, y = 3, bound = 10
 * Output: [2,3,4,5,7,9,10]
 * Explanation: 
 * 2 = 2^0 + 3^0
 * 3 = 2^1 + 3^0
 * 4 = 2^0 + 3^1
 * 5 = 2^1 + 3^1
 * 7 = 2^2 + 3^1
 * 9 = 2^3 + 3^0
 * 10 = 2^0 + 3^2
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: x = 3, y = 5, bound = 15
 * Output: [2,4,6,8,10,14]
 * 
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= x <= 100
 * 1 <= y <= 100
 * 0 <= bound <= 10^6
 * 
 */

// @lc code=start
class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        
        HashSet<Integer> result = new HashSet<>();
        int xpow = 1;
        int xpot = 0;
        while (xpow <= bound && xpot < 20) {
            int ypow = 1;
            int ypot = 0;
            while (ypow <= bound && ypot < 20) {
                if (xpow + ypow <= bound) {
                    result.add(xpow + ypow);
                }
                ypow *= y;
                ypot++;
            }
            xpow *= x;
            xpot++;
        }
        return new LinkedList<>(result);
    }
}
// @lc code=end
