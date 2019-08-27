# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P
# 利用归并算法


def merge(a, b):
    global count
    is_next = False
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            if is_next and c:
                count += len(c) - j
            c.append(a[j])
            j += 1
            is_next = True
        else:
            if is_next and c:
                count += len(c) - j
                is_next = False

            count += 1
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
        for i in a[j + 1:]:
            count += h
    print(c)
    print(count)
    return c


def merge_sort(lists):
    global count
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
    count = 0
    a = [3, 7, 8, 2, 4, 1]
    # a = [14, 7, 8, 3, 5, 9]
    print(merge_sort(a))
    print(count)
