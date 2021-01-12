'''
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
示例2:

 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        currented = {head.val}
        pos = head
        while pos.next:
            cur = pos.next
            if cur.val not in currented:
                currented.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head
"""
方法一：哈希表
我们对给定的链表进行一次遍历，并用一个哈希集合（HashSet）来存储所有出现过的节点。
由于在大部分语言中，对给定的链表元素直接进行「相等」比较，
实际上是对两个链表元素的地址（而不是值）进行比较。
因此，我们在哈希集合中存储链表元素的值，方便直接使用等号进行比较。

具体地，我们从链表的头节点 head 开始进行遍历，遍历的指针记为 pos。
由于头节点一定不会被删除，因此我们可以枚举待移除节点的前驱节点，减少编写代码的复杂度。
"""