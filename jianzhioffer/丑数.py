# 把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        res = [1]
        nextIndex = 1
        t2 = t3 = t5 = 0

        while nextIndex < index:
            min_val = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(min_val)
            while res[t2] * 2 <= min_val:
                t2 += 1
            while res[t3] * 3 <= min_val:
                t3 += 1
            while res[t5] * 5 <= min_val:
                t5 += 1
            nextIndex += 1

        return res[index - 1]
