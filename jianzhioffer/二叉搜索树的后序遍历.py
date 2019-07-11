# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# 二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树：
# 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
#  它的左、右子树也分别为二叉排序树。

# 后序遍历数组的最后一个元素为根结点

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence) <= 0:
            return False
        root = sequence[-1]
        i = 0

        # 找出左小右大的分界点i,此时i属于右子树
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1

        # 如果在右子树中有比根节点小的值，直接返回False
        for node in sequence[i:-1]:
            if node < root:
                return False
        # 判断左子树是否为二叉搜索树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        # 判断右子树是否为二叉搜索树
        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right