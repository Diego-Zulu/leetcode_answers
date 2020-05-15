/*
 * @lc app=leetcode id=204 lang=java
 *
 * [204] Count Primes
 *
 * https://leetcode.com/problems/count-primes/description/
 *
 * algorithms
 * Easy (31.04%)
 * Likes:    1793
 * Dislikes: 561
 * Total Accepted:    338.2K
 * Total Submissions: 1.1M
 * Testcase Example:  '10'
 *
 * Count the number of prime numbers less than a non-negative number, n.
 * 
 * Example:
 * 
 * 
 * Input: 10
 * Output: 4
 * Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int countPrimes(int n) {
        
        if (n==0 || n==1) return 0;
        boolean[] prime = new boolean[n];
        
        for (int i=0; i<prime.length; i++) {
            prime[i] = true;
        }
        prime[0] = false;
        prime[1] = false;
        int counter = 0;
        
        for (int i=0; i<Math.sqrt(n); i++) {
            if(prime[i]) {
                
                for (int j=i*i; j<n; j+=i) {
                    prime[j] = false;
                }
            }
        } 
        
        for (int i=0; i<prime.length; i++) {
            if (prime[i]) counter++;
        }
        
        return counter;
    }
}
// @lc code=end
