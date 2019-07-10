# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,5,3,6}和中序遍历序列{4,2,5,1,6,3}，则重建二叉树并返回
#                    1
#                  /  \
#                 2    3
#                / \  /
#               4  5 6


def rebuild_tree(pre_travel, mid_travel):
    if not pre_travel or not mid_travel:
        return None
    head = pre_travel[0]
    v = mid_travel.index(head)

    head.left = rebuild_tree(pre_travel[1:v + 1], mid_travel[:v])
    head.right = rebuild_tree(pre_travel[v + 1:], mid_travel[v + 1:])
    return head
