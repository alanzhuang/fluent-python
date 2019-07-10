# 输入两棵二叉树A和B，判断B是不是A的子结构

def isSubTree(root_a, root_b):
    result = False
    if root_a and root_b:
        if root_b.val == root_a.val:
            result = subTreeCore(root_a, root_b)
        if not result:
            result = isSubTree(root_a.left, root_b.left)
        if not result:
            result = isSubTree(root_a.right, root_b.right)
    return result


def subTreeCore(p1, p2):
    if p2 is None:
        return True
    if p1 is None:
        return False
    if p1.val != p2.val:
        return False
    return subTreeCore(p1.left, p2.left) and subTreeCore(p1.right, p2.right)
