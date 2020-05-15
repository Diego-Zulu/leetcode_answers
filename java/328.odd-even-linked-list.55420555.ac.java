/*
 * @lc app=leetcode id=328 lang=java
 *
 * [328] Odd Even Linked List
 *
 * https://leetcode.com/problems/odd-even-linked-list/description/
 *
 * algorithms
 * Medium (53.12%)
 * Likes:    1458
 * Dislikes: 277
 * Total Accepted:    221.3K
 * Total Submissions: 416.2K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * Given a singly linked list, group all odd nodes together followed by the
 * even nodes. Please note here we are talking about the node number and not
 * the value in the nodes.
 * 
 * You should try to do it in place. The program should run in O(1) space
 * complexity and O(nodes) time complexity.
 * 
 * Example 1:
 * 
 * 
 * Input: 1->2->3->4->5->NULL
 * Output: 1->3->5->2->4->NULL
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 2->1->3->5->6->4->7->NULL
 * Output: 2->3->6->7->1->5->4->NULL
 * 
 * 
 * Note:
 * 
 * 
 * The relative order inside both the even and odd groups should remain as it
 * was in the input.
 * The first node is considered odd, the second node even and so on ...
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
    public ListNode oddEvenList(ListNode head) {
        
        if (head == null) return head;
        
        ListNode h = head.next;
        ListNode lastNode = head;
        ListNode lastOddNode = head;
        boolean odd = false;
        
        while (h != null) {
            
            if (odd) {
                
                lastNode.next = h.next;
                h.next = lastOddNode.next;
                lastOddNode.next = h;
                lastOddNode = lastOddNode.next;
                h = lastNode.next;
                
            } else {
                
                lastNode = h;
                h = h.next;
                
            }
            
            odd = !odd;
            
        }
        
        return head;
    }
}
// @lc code=end
