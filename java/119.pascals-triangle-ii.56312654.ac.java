/*
 * @lc app=leetcode id=119 lang=java
 *
 * [119] Pascal's Triangle II
 *
 * https://leetcode.com/problems/pascals-triangle-ii/description/
 *
 * algorithms
 * Easy (47.89%)
 * Likes:    730
 * Dislikes: 193
 * Total Accepted:    269.7K
 * Total Submissions: 562.8K
 * Testcase Example:  '3'
 *
 * Given a non-negative index k where k ≤ 33, return the k^th index row of the
 * Pascal's triangle.
 * 
 * Note that the row index starts from 0.
 * 
 * 
 * In Pascal's triangle, each number is the sum of the two numbers directly
 * above it.
 * 
 * Example:
 * 
 * 
 * Input: 3
 * Output: [1,3,3,1]
 * 
 * 
 * Follow up:
 * 
 * Could you optimize your algorithm to use only O(k) extra space?
 * 
 */

// @lc code=start
public class Solution {
    public List<Integer> getRow(int rowIndex) {
        
        List<Integer> result = new LinkedList<>();
        result.add(1);
        
        for (int i=1; i<=rowIndex; i++) {
            
            
            for (int j=i; j>-1; j--) {
                
                int firstFactor = 0;
                int secondFactor = 0;
                
                if (j < i) {
                    firstFactor = result.get(j);
                }
                
                if (j-1 > -1) {
                    secondFactor = result.get(j-1);
                }
                
                if (j < i) {
                    result.set(j,firstFactor+secondFactor);
                } else {
                    result.add(j,firstFactor+secondFactor);
                }
            }
        }
        
        return result;
    }
}
// @lc code=end
