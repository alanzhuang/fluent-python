import functools


@functools.cmp_to_key
def cmps(a, b):
    sum_1 = str(a)+str(b)
    sum_2 = str(b)+str(a)
    if sum_1>sum_2:
        return 1
    elif sum_1 == sum_2:
        return 0
    else:
        return -1


a = [7, 22, 27, 12, 21, 2]
s = sorted(a, key=cmps)
print(''.join([str(i) for i in s]))
