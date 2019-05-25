from collections import deque

# 栈
a = [2, 4, 6, 1, 8]
a.append(777)
print(a)
print(a.pop())
print(a)

# 队列
d = deque(['a1', 'b2', 'c3'])
d.append('d4')
d.append('e5')
d.popleft()
d.popleft()
print(d)
