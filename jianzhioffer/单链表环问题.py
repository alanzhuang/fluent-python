# 如果一个链表中包含环，如何找出环的入口节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        pFast = pHead
        pSlow = pHead
        while pFast != None and pFast.next != None:
            pFast = pFast.next.next
            pSlow = pSlow.next
            # 两个指针相遇且非空，则说明有环
            if pFast == pSlow:
                break
        if pFast == None or pFast.next == None:
            return None
        pFast = pHead
        while (pFast != pSlow):
            pFast = pFast.next
            pSlow = pSlow.next
        # 返回环的入口节点
        return pFast
