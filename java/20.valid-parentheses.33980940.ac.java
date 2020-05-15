/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (38.45%)
 * Likes:    4630
 * Dislikes: 210
 * Total Accepted:    947.4K
 * Total Submissions: 2.5M
 * Testcase Example:  '"()"'
 *
 * Given a string containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * 
 * 
 * Note that an empty string is also considered valid.
 * 
 * Example 1:
 * 
 * 
 * Input: "()"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "()[]{}"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "(]"
 * Output: false
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: "([)]"
 * Output: false
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: "{[]}"
 * Output: true
 * 
 * 
 */

// @lc code=start
public class Solution {
    public boolean isValid(String s) {
        LinkedList<Character> stack = new LinkedList<Character>();
        if (s.length() == 0 || s.length()%2 != 0) return false;
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == ')') {
                if (stack.isEmpty()) return false;
                else if (stack.pop() != '(') return false;
            } else if (s.charAt(i) == ']') {
                if (stack.isEmpty()) return false;
                else if (stack.pop() != '[') return false;
            } else if (s.charAt(i) == '}') {
                if (stack.isEmpty()) return false;
                else if (stack.pop() != '{') return false;
            } else {
                stack.push(s.charAt(i));
            }
        } 
        
        return stack.isEmpty();
    }
}
// @lc code=end
