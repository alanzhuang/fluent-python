# 冒泡排序 O(n^2)

a = [4, 3, 9, 8, 6, 2, 3]
length = len(a)
for i in range(length - 1):
    print('----')
    for j in range(length - 1 - i):
        if a[j + 1] < a[j]:
            a[j], a[j + 1] = a[j + 1], a[j]
            print(a)
print(a)
