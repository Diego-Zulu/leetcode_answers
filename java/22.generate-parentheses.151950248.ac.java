/*
 * @lc app=leetcode id=22 lang=java
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (61.10%)
 * Likes:    4668
 * Dislikes: 248
 * Total Accepted:    514.8K
 * Total Submissions: 842.5K
 * Testcase Example:  '3'
 *
 * 
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 * 
 * 
 * 
 * For example, given n = 3, a solution set is:
 * 
 * 
 * [
 * ⁠ "((()))",
 * ⁠ "(()())",
 * ⁠ "(())()",
 * ⁠ "()(())",
 * ⁠ "()()()"
 * ]
 * 
 */

// @lc code=start
class Solution {
    public List<String> generateParenthesis(int n) {

        if (n <= 0) return null;

        StringBuilder parenthesis = new StringBuilder(n*2);
        List<String> combinations = new LinkedList<>();

        generateParenthesisRecursively(0, n, parenthesis, combinations);

        return combinations;
    }

    private void generateParenthesisRecursively(int openP, int n, StringBuilder parenthesis, List<String> combinations) {

        if (n > 0) {
            if (openP < n) {
                StringBuilder addingOpen = new StringBuilder(parenthesis);
                addingOpen.append('(');
                generateParenthesisRecursively(openP + 1, n, addingOpen, combinations);
            }

            if (openP > 0) {
                StringBuilder addingClosed = new StringBuilder(parenthesis);
                addingClosed.append(')');
                generateParenthesisRecursively(openP - 1, n - 1, addingClosed, combinations);
            }
        } else {
            combinations.add(parenthesis.toString());
        }
    }
}
// @lc code=end
