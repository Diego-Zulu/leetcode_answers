#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#
# https://leetcode.com/problems/design-circular-queue/description/
#
# algorithms
# Medium (42.86%)
# Likes:    484
# Dislikes: 76
# Total Accepted:    56.3K
# Total Submissions: 131.4K
# Testcase Example:  '["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n' +
  '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# Design your implementation of the circular queue. The circular queue is a
# linear data structure in which the operations are performed based on FIFO
# (First In First Out) principle and the last position is connected back to the
# first position to make a circle. It is also called "Ring Buffer".
# 
# One of the benefits of the circular queue is that we can make use of the
# spaces in front of the queue. In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the
# queue. But using the circular queue, we can use the space to store new
# values.
# 
# Your implementation should support following operations:
# 
# 
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return
# -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the
# operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the
# operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.
# 
# 
# 
# 
# Example:
# 
# 
# MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be
# 3
# circularQueue.enQueue(1);  // return true
# circularQueue.enQueue(2);  // return true
# circularQueue.enQueue(3);  // return true
# circularQueue.enQueue(4);  // return false, the queue is full
# circularQueue.Rear();  // return 3
# circularQueue.isFull();  // return true
# circularQueue.deQueue();  // return true
# circularQueue.enQueue(4);  // return true
# circularQueue.Rear();  // return 4
# 
# 
# 
# Note:
# 
# 
# All values will be in the range of [0, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in Queue library.
# 
# 
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.array = [0] * k
        self.first = 0
        self.last = k - 1
        self.k = k
        self.count = 0
        
    def next_pos(self, i):
        return (i + 1) % self.k
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        next_pos = self.next_pos(self.last)
        self.array[next_pos] = value
        self.last = next_pos
        self.count += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.first = self.next_pos(self.first)
        self.count -= 1
        return True
        

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.array[self.first]
        

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.array[self.last]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
