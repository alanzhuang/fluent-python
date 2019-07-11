# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []

        def find_road(node, path_list, total_num):
            path = list(path_list)
            total_num += node.val
            path.append(node.val)
            is_leaf = node.left is None and node.right is None
            if is_leaf and (total_num == expectNumber):
                p = []
                for i in path:
                    p.append(i)
                result.append(p)
            if total_num < expectNumber:
                 if node.left:
                    find_road(node.left, path, total_num)
                 if node.right:
                     find_road(node.right, path, total_num)
        find_road(root, [], 0)
        return result



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)

node1.left = node2
node1.right = node3
s = Solution()
print(s.FindPath(node1, 3))
