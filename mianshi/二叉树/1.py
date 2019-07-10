# 递归遍历
class Node:
    def __init__(self, val, left, right):
        self.value = val
        self.left = left
        self.right = right


def preTrval(root):
    if root is None:
        return
    print(root.value)  # 前序
    preTrval(root.left)
    # print(root.value) 放在这里就是中序遍历
    preTrval(root.right)
    # print(root.value) 放在这里就是后序遍历


# 前序遍历 不使用递归
def preTrval2(root):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# 中序遍历 不使用递归
def preTrval3(root):
    stack = []
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            node = stack.pop()
            print(node.value)
            cur = node.right
