/*
 * @lc app=leetcode id=412 lang=java
 *
 * [412] Fizz Buzz
 *
 * https://leetcode.com/problems/fizz-buzz/description/
 *
 * algorithms
 * Easy (61.72%)
 * Likes:    806
 * Dislikes: 1101
 * Total Accepted:    313.4K
 * Total Submissions: 507.8K
 * Testcase Example:  '1'
 *
 * Write a program that outputs the string representation of numbers from 1 to
 * n.
 * 
 * But for multiples of three it should output “Fizz” instead of the number and
 * for the multiples of five output “Buzz”. For numbers which are multiples of
 * both three and five output “FizzBuzz”.
 * 
 * Example:
 * 
 * n = 15,
 * 
 * Return:
 * [
 * ⁠   "1",
 * ⁠   "2",
 * ⁠   "Fizz",
 * ⁠   "4",
 * ⁠   "Buzz",
 * ⁠   "Fizz",
 * ⁠   "7",
 * ⁠   "8",
 * ⁠   "Fizz",
 * ⁠   "Buzz",
 * ⁠   "11",
 * ⁠   "Fizz",
 * ⁠   "13",
 * ⁠   "14",
 * ⁠   "FizzBuzz"
 * ]
 * 
 * 
 */

// @lc code=start
public class Solution {
    public List<String> fizzBuzz(int n) {
        
        String[] result = new String[n];
        
        FillNumbers(result, n);
        
        return Arrays.asList(result);
    }
    
    void FillNumbers(String[] toFill, int n) {
        
        int nextFiveMult = 5;
        int nextThreeMult = 3;
        
        for (int i=1; i<=n; i++) {
            
            String thisNumber = i + "";
            if (i == nextThreeMult && i == nextFiveMult) {
                nextFiveMult+=5;
                nextThreeMult+=3;
                thisNumber = "FizzBuzz";
            } else if (i == nextFiveMult) {
                nextFiveMult+=5;
                thisNumber = "Buzz";
            } else if (i == nextThreeMult) {
                nextThreeMult+=3;
                thisNumber = "Fizz";
            }
            toFill[i-1] = thisNumber;
        }
    }
}
// @lc code=end
