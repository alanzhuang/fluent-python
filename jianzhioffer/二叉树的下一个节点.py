# 题目：二叉树的下一个节点

# 题目描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  # 指向父节点


def GetNext(pNode):
    # 如果节点有右子树，那么下一个节点就是右子树的最左节点
    if pNode.right is not None:
        pNode = pNode.right
        while pNode.left:
            pNode = pNode.left
        return pNode

    # 节点是父节点的右节点
    elif pNode.next is not None and pNode.next.right == pNode:
        # 如果节点是父节点的左节点 返回父节点
        while pNode.next is not None and pNode.next.left != pNode:
            pNode = pNode.next
        return pNode.next

    # 节点是父节点的左节点 直接返回父节点
    else:
        return pNode.next
