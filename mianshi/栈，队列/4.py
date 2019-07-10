# 栈中的元素都为整型 将栈从顶到底从大到小排序，只允许申请一个栈
# 将要排序的栈叫stack, 辅助栈叫help, stack上执行pop操作，弹出元素记为cur
# 如果cur小于等于help栈顶元素，将cur直接压入hel；如果cur大于help栈顶元素，则将help元素逐一弹，逐一压入stack直到cur小于或等于help的栈
# 顶元素，再将cur压入help

def sort(stack: list):
    help = []
    while stack:
        cur = stack.pop()
        while help and help[-1] > cur:
            stack.append(help.pop())
        help.append(cur)
    while help:
        stack.append(help.pop())


s = [1, 2, 7, 5, 4, 0]
sort(s)
print(s)
