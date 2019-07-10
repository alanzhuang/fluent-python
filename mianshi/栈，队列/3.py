# 递归逆序栈
def reverse(stack):
    if not stack:
        return
    else:
        val = stack.pop(0)
        reverse(stack)
        stack.append(val)
        return stack


print(reverse([1, 2, 3, 4, 5]))


def reverseStr(str):
    if len(str) == 1:
        return str
    return reverseStr(str[1:]) + str[0]


print(reverseStr('abcde'))
