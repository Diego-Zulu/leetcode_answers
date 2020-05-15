/*
 * @lc app=leetcode id=234 lang=java
 *
 * [234] Palindrome Linked List
 *
 * https://leetcode.com/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (38.55%)
 * Likes:    2792
 * Dislikes: 337
 * Total Accepted:    391.8K
 * Total Submissions: 1M
 * Testcase Example:  '[1,2]'
 *
 * Given a singly linked list, determine if it is a palindrome.
 * 
 * Example 1:
 * 
 * 
 * Input: 1->2
 * Output: false
 * 
 * Example 2:
 * 
 * 
 * Input: 1->2->2->1
 * Output: true
 * 
 * Follow up:
 * Could you do it in O(n) time and O(1) space?
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
    public boolean isPalindrome(ListNode head) {
        
        ListNode end = null;
        ListNode index = head;
        
        while (index != null) {
            
            ListNode newNode = new ListNode(index.val);
            newNode.next = end;
            
            end = newNode;
            index = index.next;
        }
        
        if (end == null) {
            return true;
        } else {
            
            index = head;
            while (index != null) {
                
                if (index.val != end.val) {
                    return false;
                }
                index = index.next;
                end = end.next;
            }
            
            return true;
        }
    }
}
// @lc code=end
