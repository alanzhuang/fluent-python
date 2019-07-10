# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 从右上角开始找起来
def find_target(arr, target):
    row = len(arr)
    col = len(arr[0]) - 1
    i = 0
    while row > i and col >= 0:
        if target > arr[row][col]:
            row += 1
        elif target < arr[row][col]:
            col -= 1
        else:
            return True
    return False
