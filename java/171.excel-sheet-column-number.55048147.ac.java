/*
 * @lc app=leetcode id=171 lang=java
 *
 * [171] Excel Sheet Column Number
 *
 * https://leetcode.com/problems/excel-sheet-column-number/description/
 *
 * algorithms
 * Easy (53.78%)
 * Likes:    866
 * Dislikes: 144
 * Total Accepted:    276.2K
 * Total Submissions: 513.3K
 * Testcase Example:  '"A"'
 *
 * Given a column title as appear in an Excel sheet, return its corresponding
 * column number.
 * 
 * For example:
 * 
 * 
 * ⁠   A -> 1
 * ⁠   B -> 2
 * ⁠   C -> 3
 * ⁠   ...
 * ⁠   Z -> 26
 * ⁠   AA -> 27
 * ⁠   AB -> 28 
 * ⁠   ...
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "A"
 * Output: 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "AB"
 * Output: 28
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "ZY"
 * Output: 701
 * 
 */

// @lc code=start
public class Solution {
    public int titleToNumber(String s) {
        
        int columnNumber = 0;
        int sLength = s.length();
        
        for (int i=0; i<sLength; i++) {
            
            columnNumber += (s.charAt(i) - 64) * (Math.pow(26, sLength-i-1));
        }
        
        return columnNumber;
    }
}
// @lc code=end
