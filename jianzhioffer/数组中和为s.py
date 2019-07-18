# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

def FindNumbersWithSum(array, s):
    if len(array) < 2:
        return []
    min = None
    fst, lst = 0, len(array) - 1
    while fst < lst:
        sum_total = array[fst] + array[lst]
        if sum_total == s:
            if min:
                if array[fst] * array[lst] < min:
                    min = array[fst] * array[lst]
                    min_i, min_j = fst, lst
            else:
                min = array[fst] * array[lst]
                min_i, min_j = fst, lst
            fst += 1
            lst -= 1
        elif sum_total < s:
            fst += 1
        else:
            lst -= 1
    if min:
        print([array[min_i], array[min_j]])
    else:
        print([])


FindNumbersWithSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 99)
