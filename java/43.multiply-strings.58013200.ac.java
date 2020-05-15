/*
 * @lc app=leetcode id=43 lang=java
 *
 * [43] Multiply Strings
 *
 * https://leetcode.com/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (33.20%)
 * Likes:    1604
 * Dislikes: 736
 * Total Accepted:    278.4K
 * Total Submissions: 838K
 * Testcase Example:  '"2"\n"3"'
 *
 * Given two non-negative integers num1 and num2 represented as strings, return
 * the product of num1 and num2, also represented as a string.
 * 
 * Example 1:
 * 
 * 
 * Input: num1 = "2", num2 = "3"
 * Output: "6"
 * 
 * Example 2:
 * 
 * 
 * Input: num1 = "123", num2 = "456"
 * Output: "56088"
 * 
 * 
 * Note:
 * 
 * 
 * The length of both num1 and num2 is < 110.
 * Both num1 and num2 contain only digits 0-9.
 * Both num1 and num2 do not contain any leading zero, except the number 0
 * itself.
 * You must not use any built-in BigInteger library or convert the inputs to
 * integer directly.
 * 
 * 
 */

// @lc code=start
public class Solution {
    public String multiply(String num1, String num2) {
        
        if(num1.equals("0") || num2.equals("0")) return "0";
        
        int n = num1.length();
        int m= num2.length();
        int firstPos;
        int mul;
        int[] carry = new int[n+m];
        StringBuilder r = new StringBuilder();
        
        for (int i=n-1; i>-1;i--) {
            for (int j=m-1; j>-1; j--) {
                
                mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                firstPos = j+i+1;
                
                mul+=carry[firstPos];
                
                carry[firstPos]=mul%10;
                carry[j+i]+=mul/10;
            }
        }
        int nm=n+m;
        boolean onTrailingZero=true;
        for(int i=0; i<nm;i++){
            if(!onTrailingZero){
                r.append(carry[i]);
            } else if (carry[i]!=0){
            onTrailingZero=false;
            r.append(carry[i]);
            }
        }
        return r.toString();
    }
}
// @lc code=end
