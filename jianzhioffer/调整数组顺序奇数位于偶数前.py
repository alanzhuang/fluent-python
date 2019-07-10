# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

# 解题思路：使用两个指针，第一个指针初始化指向数组的第一个数字，从前向后移动，遇到偶数就停下来；
# 第二个指针指向数组的最后一个数字，从后向前移动，遇到奇数就停下来，交换两个指针指向的元素，直到两个指针相遇。

def reOrder(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        while start < end and not isEven(arr[start]):
            start += 1
        while start < end and isEven(arr[end]):
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    return arr


def isEven(val):
    return val % 2 == 0

print(reOrder([123,432,33,423,6,9,23,87,32,2]))