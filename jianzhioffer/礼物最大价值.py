# 在一个mxn的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0），你可以从棋盘的左上角开始拿格子里的礼物，
# 并每次向右或者向下移动一格，直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿多少价值的礼物？

# 递归太慢 有很多重复运算

def get_max(arr, i, j):
    if i == 0 and j == 0:
        return arr[0][0]
    elif i == 0:
        return get_max(arr, 0, j - 1) + arr[i][j]
    elif j == 0:
        return get_max(arr, i - 1, 0) + arr[i][j]
    return max(get_max(arr, i - 1, j), get_max(arr, i, j - 1)) + arr[i][j]


# 申请一个二维数组arr2 和原来数组大小一样 然后arr[i][j]保存此格礼物的最大值

def get_max2(arr, rows, cols):
    arr2 = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            up = 0
            left = 0
            if i > 0:
                up = arr2[i - 1][j]
            if j > 0:
                left = arr2[j][j - 1]
            arr2[i][j] = max(up, left) + arr[i][j]
    return arr2[rows - 1][cols - 1]


# 进一步节约空间 申请一维数组 保存值
def get_max3(arr, rows, cols):
    arr2 = [0 for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            up = 0
            left = 0
            if i > 0:
                up = arr2[j]
            if j > 0:
                left = arr2[j - 1]
            arr2[j] = max(up, left) + arr[i][j]
    return arr2[cols - 1]


myList = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
sss = get_max3(myList, 4, 4)
print(sss)
