/*
 * @lc app=leetcode id=23 lang=java
 *
 * [23] Merge k Sorted Lists
 *
 * https://leetcode.com/problems/merge-k-sorted-lists/description/
 *
 * algorithms
 * Hard (39.15%)
 * Likes:    4275
 * Dislikes: 271
 * Total Accepted:    605.7K
 * Total Submissions: 1.5M
 * Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
 *
 * Merge k sorted linked lists and return it as one sorted list. Analyze and
 * describe its complexity.
 * 
 * Example:
 * 
 * 
 * Input:
 * [
 * 1->4->5,
 * 1->3->4,
 * 2->6
 * ]
 * Output: 1->1->2->3->4->4->5->6
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        
       PriorityQueue<Integer> orderedElements = new PriorityQueue<>();
        
        for (ListNode l : lists) {
            while (l != null) {
                orderedElements.add(l.val);
                l = l.next;
            }
        }
        if (orderedElements.isEmpty())  return null;
        
        ListNode merged = new ListNode(orderedElements.poll());
        ListNode aux = merged;
        
        while (!orderedElements.isEmpty()) {
            aux.next = new ListNode(orderedElements.poll());
            aux = aux.next;
        }
        
        return merged;
    }
}
// @lc code=end
