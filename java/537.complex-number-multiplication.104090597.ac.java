/*
 * @lc app=leetcode id=537 lang=java
 *
 * [537] Complex Number Multiplication
 *
 * https://leetcode.com/problems/complex-number-multiplication/description/
 *
 * algorithms
 * Medium (66.97%)
 * Likes:    223
 * Dislikes: 693
 * Total Accepted:    45.5K
 * Total Submissions: 67.8K
 * Testcase Example:  '"1+1i"\n"1+1i"'
 *
 * 
 * Given two strings representing two complex numbers.
 * 
 * 
 * You need to return a string representing their multiplication. Note i^2 = -1
 * according to the definition.
 * 
 * 
 * Example 1:
 * 
 * Input: "1+1i", "1+1i"
 * Output: "0+2i"
 * Explanation: (1 + i) * (1 + i) = 1 + i^2 + 2 * i = 2i, and you need convert
 * it to the form of 0+2i.
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: "1+-1i", "1+-1i"
 * Output: "0+-2i"
 * Explanation: (1 - i) * (1 - i) = 1 + i^2 - 2 * i = -2i, and you need convert
 * it to the form of 0+-2i.
 * 
 * 
 * 
 * Note:
 * 
 * The input strings will not have extra blank.
 * The input strings will be given in the form of a+bi, where the integer a and
 * b will both belong to the range of [-100, 100]. And the output should be
 * also in this form.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public String complexNumberMultiply(String a, String b) {
        
        int indexOfPlusSignInA = a.indexOf("+");
        int indexOfPlusSignInB = b.indexOf("+");
        int aNumber = Integer.parseInt(a.substring(0, indexOfPlusSignInA ));
        int bNumber = Integer.parseInt(a.substring(indexOfPlusSignInA + 1, a.length() - 1));
        int cNumber = Integer.parseInt(b.substring(0, indexOfPlusSignInB ));
        int dNumber = Integer.parseInt(b.substring(indexOfPlusSignInB + 1, b.length() - 1));
        
        int imaginarySum = aNumber * dNumber + bNumber * cNumber;
        int realSum = aNumber * cNumber + bNumber * dNumber * -1;
        
        return realSum + "+" + imaginarySum + "i";
    }
}
// @lc code=end
