def PrintFromTopToBottom(root):
    if not root:
        return
    res = []
    res.append(root)
    res_val = []
    while res:
        node = res.pop(0) # pop(0)时间复杂度O(N) 后面元素发生位移
        res_val.append(node.val)
        if node.left:
            res.append(node.left)
        elif node.right:
            res.append(node.right)
    return res_val
