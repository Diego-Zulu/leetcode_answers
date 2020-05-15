/*
 * @lc app=leetcode id=56 lang=java
 *
 * [56] Merge Intervals
 *
 * https://leetcode.com/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (38.53%)
 * Likes:    3728
 * Dislikes: 270
 * Total Accepted:    556.1K
 * Total Submissions: 1.4M
 * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
 *
 * Given a collection of intervals, merge all overlapping intervals.
 * 
 * Example 1:
 * 
 * 
 * Input: [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 * Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
 * [1,6].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [[1,4],[4,5]]
 * Output: [[1,5]]
 * Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 * 
 * NOTE: input types have been changed on April 15, 2019. Please reset to
 * default code definition to get new method signature.
 * 
 */

// @lc code=start
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        
        List<Interval> result = new LinkedList<>();
        HashMap<Integer, Integer> startToEnd = new HashMap<>();
        
        if (intervals == null || intervals.size() < 1) return result;
        
        int[] test = new int[intervals.size()];
        int i=0;
        for (Interval inter : intervals) {
            int end = startToEnd.getOrDefault(inter.start, inter.end);
            startToEnd.put(inter.start, end < inter.end ? inter.end : end);
            test[i] = inter.start;
            i++;
        }
        
        Arrays.sort(test);
        
        int start = test[0];
        int end = startToEnd.get(start);
        
        for (int interStart : test) {
            if (interStart <= end) {
                end = Math.max(end, startToEnd.get(interStart));
            } else {
                result.add(new Interval(start, end));
                start = interStart;
                end = startToEnd.get(interStart);
            }
        }
        result.add(new Interval(start, end));
        
        return result;
    }
}
// @lc code=end
