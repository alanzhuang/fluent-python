# 二分查找 O(logn)
a = [2, 3, 6, 19, 88, 122, 888]


def find(alist, val):
    start = 0
    end = len(alist)
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] < val:
            start = mid + 1
        elif alist[mid] > val:
            end = mid - 1
        else:
            return True
    return False


val = input('需要查找的数值：')
msg = '找到了' if find(a, int(val)) else '木有'
print(msg)
