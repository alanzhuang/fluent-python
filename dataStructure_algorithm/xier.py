# 希尔排序 O(n^(1.3—2)) 和增量因子有关
# https://blog.csdn.net/weixin_37818081/article/details/79202115
import random
import time


def insertion_sort(list, step):
    '''插入排序'''
    # 类似冒泡排序
    for i in range(step, len(list)):
        for j in range(i, step - 1, -step):
            if list[j] < list[j - step]:
                list[j], list[j - step] = list[j - step], list[j]
            else:
                break


def sort(list):
    '''希尔排序'''
    length = len(list)
    step = 1

    while step < length // 3:
        step = 3 * step + 1  # 为了保证可以缩小到1而不是0，所有+1

    while step >= 1:
        insertion_sort(list, step)
        step = step // 3


if __name__ == "__main__":
    l = [random.randint(0, 100) for _ in range(20)]

    start = time.time()
    sort(l)
    print(l)
    end = time.time()

    print(end - start)