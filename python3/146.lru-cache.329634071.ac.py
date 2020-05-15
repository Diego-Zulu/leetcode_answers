#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (31.91%)
# Likes:    5403
# Dislikes: 243
# Total Accepted:    522.3K
# Total Submissions: 1.6M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

# @lc code=start
class DoubleNode:
    def __init__(self, k, x):
        self.key = k
        self.val = x
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used_head = DoubleNode(-1, -1)
        self.used_tail = DoubleNode(-1, -1)
        self.used_head.next = self.used_tail
        self.used_tail.prev = self.used_head
        self.used = {}

    def get(self, key: int) -> int:
        if key not in self.used:
            return -1
        n = self.used[key]
        self._change_head(n)
        return n.val
        
    def _change_head(self, node):
        if node.key in self.used:
            node.prev.next = node.next
            node.next.prev = node.prev
        next_ = self.used_head.next
        next_.prev = node
        node.next = next_
        node.prev = self.used_head
        self.used_head.next = node
        
    def _pop_tail(self):
        prev = self.used_tail.prev
        prev.prev.next = prev.next
        prev.next.prev = prev.prev
        return prev.key

    def put(self, key: int, value: int) -> None:
        if key in self.used:
            self.capacity += 1
            node = self.used[key]
            node.val = value
        else:
            node = DoubleNode(key, value)
        self._change_head(node)
        self.capacity -= 1
        self.used[key] = node
        if self.capacity < 0:
            self.capacity = 0
            del self.used[self._pop_tail()]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
