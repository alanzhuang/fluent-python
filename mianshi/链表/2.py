# 删除单链表倒数第k个节点
# 快慢指针 快指针先走k步，等快指针到最后一个节点时，慢指针就在倒数k+1个节点

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


def del_node(head: Node, k):
    h1 = head
    h2 = head
    while k:
        h1 = h1.next
        if not h1:
            head = head.next
            return head
        k -= 1
    while h1:
        h1 = h1.next
        h2 = h2.next
    h2.next = h2.next.next
    return head


# 删除中间的节点
def del_mid_node(head: Node, k):
    if head.next is None:
        return head
    if head.next.next is None:
        return head.next
    h1 = head
    h2 = head.next.next
    while h1.next and h2.next.next:
        h1 = h1.next
        h2 = h2.next.next
    h1.next = h1.next.next
    return head


# 反转链表
def reverse(head: Node):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


# 反转from到to位置的部分链表
def reverse_part(head: Node, frm: int, to: int):
    count = 0
    node1 = head
    fPre = None
    tPos = None
    while node1:
        count += 1
        fPre = node1 if count == frm - 1 else fPre
        tPos = node1 if count == to + 1 else tPos
    node1 = head if fPre is None else fPre.next #需要反转链表的头节点
    node2 = node1.next
    node1.next = tPos
    next = None
    while node2:
        next = node2.next
        node2.next = node1
        node1 = node2
        node2 = next
    if fPre is not None:
        fPre.next = node1
        return head
    return node1