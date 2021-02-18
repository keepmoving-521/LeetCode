"""
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4
"""
#  方法一：
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        p = head
        for i in range(k):
            p = p.next
        while p:
            head = head.next
            p=p.next
        return head.val

#  方法二：
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        if not head:
            return None
        data = []
        while head:
            data.append(head.val)
            head = head.next
        return data[-k]


"""
方法一：
解题思路
在不知道链表长度的情况下，需要知道倒数第k个节点可以借助一个临时节点p,让他先走k步。
然后head和p一起往后移，当p走到末尾的时候，head指向的节点就是我们要求的节点。
方法二：
解题思路
遍历链表，将value存入一个数组
"""