t1 = (1, 2, [3])
t2 = (1, 2, [3])

print(t1 == t2) # TRUE
print(id(t1[-1]))
t1[-1].append(4) # 用+=会报错 不知道为啥 明明都是就地改动- -？
# https://blog.csdn.net/weixin_34242509/article/details/88986468
# +=不是原子操作 t1[-1].extend([4]) t[-1] = t[-1]
# 第二步有赋值操作会报错

print(id(t1[-1])) # 和上面的id意义
print(t1)
print(t1 == t2) # FALSE

