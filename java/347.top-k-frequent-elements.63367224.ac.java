/*
 * @lc app=leetcode id=347 lang=java
 *
 * [347] Top K Frequent Elements
 *
 * https://leetcode.com/problems/top-k-frequent-elements/description/
 *
 * algorithms
 * Medium (59.83%)
 * Likes:    2712
 * Dislikes: 198
 * Total Accepted:    357.9K
 * Total Submissions: 598K
 * Testcase Example:  '[1,1,1,2,2,3]\n2'
 *
 * Given a non-empty array of integers, return the k most frequent elements.
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,1,1,2,2,3], k = 2
 * Output: [1,2]
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1], k = 1
 * Output: [1]
 * 
 * 
 * Note: 
 * 
 * 
 * You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 * Your algorithm's time complexity must be better than O(n log n), where n is
 * the array's size.
 * It's guaranteed that the answer is unique, in other words the set of the top
 * k frequent elements is unique.
 * You can return the answer in any order.
 * 
 * 
 */

// @lc code=start
public class Solution {
    
    public List<Integer> topKFrequent(int[] nums, int k) {
         
        int n = nums.length;
        List<Integer> answer = new LinkedList<>();
        Map<Integer, Integer> frecuencies = new HashMap<>();
        LinkedList<Integer>[] orderFrecuencies = new LinkedList[n+1];
        
        if (n == 0) return answer;
        
        for (int i=0; i<n; i++) {
            
            frecuencies.put(nums[i], frecuencies.getOrDefault(nums[i], 0) + 1);
        }
        
        for (int s : frecuencies.keySet()) {
            
            int number = frecuencies.get(s);
            if (orderFrecuencies[number] == null) {
                orderFrecuencies[number] = new LinkedList<>();
            }
            orderFrecuencies[number].add(s);
        }
        
        for (int i=n; i>=0 && answer.size() < k; i--) {
            
            while (answer.size() < k && orderFrecuencies[i] != null && !orderFrecuencies[i].isEmpty()) {
                int actual = orderFrecuencies[i].remove();
                answer.add(actual);
            }
        }
        
        return answer;
    }
}
// @lc code=end
