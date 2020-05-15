/*
 * @lc app=leetcode id=6 lang=java
 *
 * [6] ZigZag Conversion
 *
 * https://leetcode.com/problems/zigzag-conversion/description/
 *
 * algorithms
 * Medium (35.44%)
 * Likes:    1542
 * Dislikes: 4365
 * Total Accepted:    438.4K
 * Total Submissions: 1.2M
 * Testcase Example:  '"PAYPALISHIRING"\n3'
 *
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
 * of rows like this: (you may want to display this pattern in a fixed font for
 * better legibility)
 * 
 * 
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * 
 * 
 * And then read line by line: "PAHNAPLSIIGYIR"
 * 
 * Write the code that will take a string and make this conversion given a
 * number of rows:
 * 
 * 
 * string convert(string s, int numRows);
 * 
 * Example 1:
 * 
 * 
 * Input: s = "PAYPALISHIRING", numRows = 3
 * Output: "PAHNAPLSIIGYIR"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "PAYPALISHIRING", numRows = 4
 * Output: "PINALSIGYAHRPI"
 * Explanation:
 * 
 * P     I    N
 * A   L S  I G
 * Y A   H R
 * P     I
 * 
 */

// @lc code=start
public class Solution {
    public String convert(String s, int numRows) {
        
        String result = "";
        int sLength = s.length();
        boolean goingDown = true;
        
        if (numRows == 1) return s;
        
        for (int i=1; i<=numRows; i++) {
            
            for (int j=i-1; j<sLength;goingDown = !goingDown) {
                
                result = result + s.charAt(j);
                
                if (i==1) {
                    
                    j+=(numRows-i)*2;
                } else if (i==numRows) {
                    
                    j+=(i-1)*2;
                } else {
                    if (goingDown) {
                        j+=(numRows-i)*2;
                    } else {
                        j+=(i-1)*2;
                    }
                }
                
            }
            goingDown = true;
        }
        
        return result;
    }
}
// @lc code=end
