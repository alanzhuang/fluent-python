# 输入一个整形数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O（n）
def test(s):
    cur_max = s[0]
    sum = 0

    for i in s:
        if sum < 0:
            sum = i
        else:
            sum += i
        if sum > cur_max:
            cur_max = sum
    return cur_max


myList = [-1, -3, -3]
sss = test(myList)
print(sss)
