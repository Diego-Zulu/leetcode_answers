/*
 * @lc app=leetcode id=686 lang=java
 *
 * [686] Repeated String Match
 *
 * https://leetcode.com/problems/repeated-string-match/description/
 *
 * algorithms
 * Easy (32.15%)
 * Likes:    726
 * Dislikes: 696
 * Total Accepted:    88.2K
 * Total Submissions: 274.3K
 * Testcase Example:  '"abcd"\n"cdabcdab"'
 *
 * Given two strings A and B, find the minimum number of times A has to be
 * repeated such that B is a substring of it. If no such solution, return -1.
 * 
 * For example, with A = "abcd" and B = "cdabcdab".
 * 
 * Return 3, because by repeating A three times (“abcdabcdabcd”), B is a
 * substring of it; and B is not a substring of A repeated two times
 * ("abcdabcd").
 * 
 * Note:
 * The length of A and B will be between 1 and 10000.
 * 
 */

// @lc code=start
class Solution {
    public int repeatedStringMatch(String A, String B) {

        int timesRepeated = 1;
        StringBuilder sb = new StringBuilder(A);
        
        while (sb.length() < B.length()) {
            sb.append(A);
            timesRepeated++;
        }
        
        if (sb.toString().contains(B)) return timesRepeated;
        if (sb.append(A).toString().contains(B)) return timesRepeated + 1;
        
        return -1;
    }
}
// @lc code=end
