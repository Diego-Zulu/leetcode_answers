/*
 * @lc app=leetcode id=67 lang=java
 *
 * [67] Add Binary
 *
 * https://leetcode.com/problems/add-binary/description/
 *
 * algorithms
 * Easy (43.28%)
 * Likes:    1597
 * Dislikes: 262
 * Total Accepted:    424.7K
 * Total Submissions: 980.6K
 * Testcase Example:  '"11"\n"1"'
 *
 * Given two binary strings, return their sum (also a binary string).
 * 
 * The input strings are both non-empty and contains only characters 1 or 0.
 * 
 * Example 1:
 * 
 * 
 * Input: a = "11", b = "1"
 * Output: "100"
 * 
 * Example 2:
 * 
 * 
 * Input: a = "1010", b = "1011"
 * Output: "10101"
 * 
 * 
 * Constraints:
 * 
 * 
 * Each string consists only of '0' or '1' characters.
 * 1 <= a.length, b.length <= 10^4
 * Each string is either "0" or doesn't contain any leading zero.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public String addBinary(String a, String b) {
        
        int ia = transformToInt(a); 
        int ib = transformToInt(b);
    
        return transformToBinaryString(ia + ib);
        
    }
    
    public int transformToInt(String aux) {
        
        int transformed = 0;
        for (int i=0; i<aux.length(); i++) {
            
            transformed += ( (aux.charAt ( aux.length() - i - 1 ) - '0') << i);
        }
        
        return transformed;
    }
    
    public String transformToBinaryString(int aux) {
        
        StringBuilder transformed = new StringBuilder();
        boolean trailingZeroes = true;
        for (int i=31; i>=0; i--) {
            
            int currentNumber = (aux >> i) & 1;
            
            if (trailingZeroes) {
                if (currentNumber == 1) {
                    trailingZeroes = false;
                } else {
                    continue;
                }
            } 
            
            transformed.append(currentNumber);
        }
        
        if (trailingZeroes) {
            return "0";
        }
        
        return transformed.toString();
    }
}
// @lc code=end
