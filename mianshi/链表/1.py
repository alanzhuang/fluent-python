# 打印两个有序链表的公共部分
# 各自的头部分别为head1,head2。如果head1小于head2，head1向下移动，head1大于head2，head2向下移动
# 如果head1和head2相等，打印这个值然后2个同时向下移动

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


def print_commom_part(head1: Node, head2: Node):
    while head1 and head2:
        if head1.value < head2.value:
            head1 = head1.next
        elif head1.value > head2.value:
            head2 = head2.next
        else:
            print('comm value:' + str(head2.value))
            head2 = head2.next
            head1 = head1.next
