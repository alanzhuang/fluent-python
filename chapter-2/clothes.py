color = ['yellow', 'black']
size = ['s', 'm', 'l']
c = [(m, n) for m in color for n in size]
print(c)

# 生成器
d = ((m,n) for m in color for n in size)
