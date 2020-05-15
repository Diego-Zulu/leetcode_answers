/*
 * @lc app=leetcode id=453 lang=java
 *
 * [453] Minimum Moves to Equal Array Elements
 *
 * https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
 *
 * algorithms
 * Easy (49.87%)
 * Likes:    515
 * Dislikes: 746
 * Total Accepted:    70.2K
 * Total Submissions: 140.7K
 * Testcase Example:  '[1,2,3]'
 *
 * Given a non-empty integer array of size n, find the minimum number of moves
 * required to make all array elements equal, where a move is incrementing n -
 * 1 elements by 1.
 * 
 * Example:
 * 
 * Input:
 * [1,2,3]
 * 
 * Output:
 * 3
 * 
 * Explanation:
 * Only three moves are needed (remember each move increments two elements):
 * 
 * [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
 * 
 * 
 */

// @lc code=start
public class Solution {
    public int minMoves(int[] nums) {
        
        int sum = 0;
        int min = Integer.MAX_VALUE;
        
        for (int number : nums) {
            min = Integer.min(number, min);
            sum += number;
        }
        
        return sum - min * nums.length;
    }
}
// @lc code=end
