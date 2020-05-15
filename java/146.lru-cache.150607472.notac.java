/*
 * @lc app=leetcode id=146 lang=java
 *
 * [146] LRU Cache
 *
 * https://leetcode.com/problems/lru-cache/description/
 *
 * algorithms
 * Medium (31.91%)
 * Likes:    5403
 * Dislikes: 243
 * Total Accepted:    522.3K
 * Total Submissions: 1.6M
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * Design and implement a data structure for Least Recently Used (LRU) cache.
 * It should support the following operations: get and put.
 * 
 * get(key) - Get the value (will always be positive) of the key if the key
 * exists in the cache, otherwise return -1.
 * put(key, value) - Set or insert the value if the key is not already present.
 * When the cache reached its capacity, it should invalidate the least recently
 * used item before inserting a new item.
 * 
 * The cache is initialized with a positive capacity.
 * 
 * Follow up:
 * Could you do both operations in O(1) time complexity?
 * 
 * Example:
 * 
 * 
 * LRUCache cache = new LRUCache( 2 /* capacity */ );
 * 
 * cache.put(1, 1);
 * cache.put(2, 2);
 * cache.get(1);       // returns 1
 * cache.put(3, 3);    // evicts key 2
 * cache.get(2);       // returns -1 (not found)
 * cache.put(4, 4);    // evicts key 1
 * cache.get(1);       // returns -1 (not found)
 * cache.get(3);       // returns 3
 * cache.get(4);       // returns 4
 * 
 * 
 * 
 * 
 */

// @lc code=start
class LRUCache {

    class LinkedNode<T> {
    
    public LinkedNode prev;
    public LinkedNode next;
    public T value;
    public T key;
    
    public LinkedNode() {
        prev = null;
        next = null;
        
    }
    
    public LinkedNode(T k, T val) {
        prev = null;
        next = null;
        value = val;
        key = k;
    }
}
    
    LinkedNode<Integer> oldestKey;
    LinkedNode<Integer> newestKey;
    HashMap<Integer, LinkedNode<Integer>> cache;
    int cap;
    int count;

    public LRUCache(int capacity) {
        oldestKey = newestKey = null;
        cap = capacity;
        count = 0;
        cache = new HashMap<>(capacity);
    }
    
    public int get(int key) {
        
        if (!cache.containsKey(key)) {
            return -1;
        } else {
            LinkedNode<Integer> value = cache.get(key);
            updateKeyNewness(value);
        
            return value.value;
        }
        
    }
    
    private void updateKeyNewness(LinkedNode<Integer> value) {
        LinkedNode<Integer> next = value.next;
        
        if (value.prev != null) {
            value.prev.next = value.next;
        }
        
        if (next != null) {
            next.prev = value.prev;
        }
        
        setNodeAsNewest(value);

        
        if (value == oldestKey) {
            oldestKey = next;
        } 
        
        if (oldestKey == null) {
            oldestKey = newestKey;
        }
    }
    
    private void setNodeAsNewest(LinkedNode<Integer> value) {
        newestKey.next = value;
        value.prev = newestKey;
        newestKey = value;
    }
    
    public void put(int key, int value) {
        
        LinkedNode<Integer> node = new LinkedNode<>(key, value);
        cache.put(key, node);
        
        if (newestKey == null) {
            newestKey = oldestKey = node;
        }
        else {
        
             setNodeAsNewest(node);

            if (count + 1 == cap) {
                cache.remove(oldestKey.key);

                if (oldestKey.next != null) {
                    oldestKey.next.prev = null;
                }
                oldestKey = oldestKey.next;
            } else {
                count++;
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end
