/*
 * @lc app=leetcode id=150 lang=java
 *
 * [150] Evaluate Reverse Polish Notation
 *
 * https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
 *
 * algorithms
 * Medium (35.40%)
 * Likes:    905
 * Dislikes: 441
 * Total Accepted:    216.7K
 * Total Submissions: 611.6K
 * Testcase Example:  '["2","1","+","3","*"]'
 *
 * Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 * 
 * Valid operators are +, -, *, /. Each operand may be an integer or another
 * expression.
 * 
 * Note:
 * 
 * 
 * Division between two integers should truncate toward zero.
 * The given RPN expression is always valid. That means the expression would
 * always evaluate to a result and there won't be any divide by zero
 * operation.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: ["2", "1", "+", "3", "*"]
 * Output: 9
 * Explanation: ((2 + 1) * 3) = 9
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: ["4", "13", "5", "/", "+"]
 * Output: 6
 * Explanation: (4 + (13 / 5)) = 6
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
 * Output: 22
 * Explanation: 
 * ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
 * = ((10 * (6 / (12 * -11))) + 17) + 5
 * = ((10 * (6 / -132)) + 17) + 5
 * = ((10 * 0) + 17) + 5
 * = (0 + 17) + 5
 * = 17 + 5
 * = 22
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> rpn = new Stack<>();
        int firstPop = 0;
        
        for (int i=0; i<tokens.length; i++) {
            
            switch (tokens[i]) {
                
                case "+" : 
                    firstPop = rpn.pop();
                    rpn.push(rpn.pop() + firstPop);
                    break;
                case "-" : 
                    firstPop = rpn.pop();
                    rpn.push(rpn.pop() - firstPop);
                    break;
                case "/" : 
                    firstPop = rpn.pop();
                    rpn.push(rpn.pop() / firstPop);
                    break;
                case "*" : 
                    firstPop = rpn.pop();
                    rpn.push(rpn.pop() * firstPop);
                    break;
                default:
                    rpn.push(Integer.parseInt(tokens[i]));
            }
        }
        
        return rpn.pop();
    }
}
// @lc code=end
