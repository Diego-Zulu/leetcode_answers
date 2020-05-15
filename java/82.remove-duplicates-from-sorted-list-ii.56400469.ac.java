/*
 * @lc app=leetcode id=82 lang=java
 *
 * [82] Remove Duplicates from Sorted List II
 *
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
 *
 * algorithms
 * Medium (35.91%)
 * Likes:    1447
 * Dislikes: 103
 * Total Accepted:    237.4K
 * Total Submissions: 660.6K
 * Testcase Example:  '[1,2,3,3,4,4,5]'
 *
 * Given a sorted linked list, delete all nodes that have duplicate numbers,
 * leaving only distinct numbers from the original list.
 * 
 * Return the linked list sorted as well.
 * 
 * Example 1:
 * 
 * 
 * Input: 1->2->3->3->4->4->5
 * Output: 1->2->5
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 1->1->1->2->3
 * Output: 2->3
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
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        
        if (head == null) return head;
        ListNode h = head;
        ListNode result = null;
        ListNode returnNode = result;
        int lastNumber = h.val-1;
        
        while (h != null) {
            
            if (h.val != lastNumber && (h.next != null && h.next.val != h.val) || h.val != lastNumber && h.next == null) {
                
                if (result == null) {
                    
                    returnNode = new ListNode(h.val);
                    result = returnNode;
                } else {
                    result.next = new ListNode(h.val);
                    result = result.next;
                }
            }
            
            lastNumber = h.val;
            h = h.next;
            
        }
        
        return returnNode;
    }
}
// @lc code=end
