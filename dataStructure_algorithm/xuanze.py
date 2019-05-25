# 简单选择排序 O(n^2)

# 虽然选择排序和冒泡排序的时间复杂度一样，但实际上，选择排序进行的交换操作很少，最多会发生 N - 1次交换。
# 而冒泡排序最坏的情况下要发生N^2 /2交换操作。从这个意义上讲，交换排序的性能略优于冒泡排序。
# 而且，交换排序比冒泡排序的思想更加直观。
a = [4, 3, 9, 8, 6, 2, 3]


def select_sort(origin_items, comp=lambda x, y: x < y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
        print(items)
    return items


print(select_sort(a))
