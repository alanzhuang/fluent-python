# 生成窗口最大数组 5.jpg 时间复杂度O(N)
import collections


def getMaxWindow(arr: list, w: int):
    qmax = collections.deque()
    out_put = []
    for i in range(0, len(arr)):
        while qmax and arr[qmax[-1]] <= arr[i]:
            qmax.pop()
        qmax.append(i)
        if qmax[0] == i - w:
            qmax.popleft()
        if i >= w - 1:
            out_put.append(arr[qmax[0]])
    return out_put


s = getMaxWindow([4, 3, 5, 4, 3, 3, 6, 7], 3)
print(s)
