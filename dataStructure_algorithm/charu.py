# 插入排序 O(n^2)

def InsertSort(s):
    # 获取列表长度
    length = len(s)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if s[j] >= s[j - 1]:
                break
            else:
                s[j], s[j - 1] = s[j - 1], s[j]
    return s


myList = [111, 38, 65, 97, 76, 13, 27, 49]
InsertSort(myList)
print(myList)
