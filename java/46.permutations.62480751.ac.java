/*
 * @lc app=leetcode id=46 lang=java
 *
 * [46] Permutations
 *
 * https://leetcode.com/problems/permutations/description/
 *
 * algorithms
 * Medium (61.75%)
 * Likes:    3471
 * Dislikes: 100
 * Total Accepted:    566.1K
 * Total Submissions: 916K
 * Testcase Example:  '[1,2,3]'
 *
 * Given a collection of distinct integers, return all possible permutations.
 * 
 * Example:
 * 
 * 
 * Input: [1,2,3]
 * Output:
 * [
 * ⁠ [1,2,3],
 * ⁠ [1,3,2],
 * ⁠ [2,1,3],
 * ⁠ [2,3,1],
 * ⁠ [3,1,2],
 * ⁠ [3,2,1]
 * ]
 * 
 * 
 */

// @lc code=start
public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        
        int n = nums.length;
        List<List<Integer>> answer = new LinkedList<>();
        
        if (n == 0) return answer;
        List<Integer> first = new LinkedList<Integer>();
        int currentNumber = nums[0];
        first.add(currentNumber);
        answer.add(first);
        int currentNumberOfList = 1;
        
        for (int i=1; i<n; i++) {
            
            currentNumber = nums[i];
            currentNumberOfList*=i;
            for (int j=0; j<currentNumberOfList; j++) {
                
                List<Integer> current = answer.remove(0);
                int currentListLength = i+1;
                for (int c=0; c<currentListLength; c++) {
                    
                    List<Integer> cloned = cloneLinkedList(current, i);
                    cloned.add(c, currentNumber);
                    answer.add(cloned);
                }
            }
        }
        
        return answer;
    }
    
    private List<Integer> cloneLinkedList(List<Integer> toBeCloned, int length) {
        
       List<Integer> cloned = new LinkedList<>();
        for (int i=0; i<length; i++) {
            
            int copiedValue = toBeCloned.get(i);
            cloned.add(copiedValue);
        }
        return cloned;
    }
}
// @lc code=end
