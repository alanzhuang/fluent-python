# 堆排序 时间复杂度O(nlogn)
# https://www.cnblogs.com/0zcl/p/6737944.html
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def sift_down(array, start, end):
    while True:
        left_child = 2 * start + 1
        if left_child > end:
            break
        if left_child + 1 <= end and array[left_child + 1] > array[left_child]:
            left_child += 1
        if array[left_child] > array[start]:  # 当左右孩子的最大值大于父结点时，则交换
            array[left_child], array[start] = swap(array[left_child], array[start])
            start = left_child  # 交换之后以交换子结点为根的堆可能不是大顶堆，需重新调整
        else:
            break
        print(">>", array)


def heap_sort(array):
    first = len(array) // 2 - 1
    for i in range(first, -1, -1):
        sift_down(array, i, len(array) - 1)
    for head_end in range(len(array) - 1, 0, -1):
        array[head_end], array[0] = swap(array[head_end], array[0])
        sift_down(array, 0, head_end - 1)


if __name__ == '__main__':
    array = [16, 66, 99, 2, 12, 132, 122, 22, 333]
    heap_sort(array)
    print(array)
