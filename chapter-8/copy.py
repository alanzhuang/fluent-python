a = [0, [1, 2], (3, 4)]
b = list(a)
a.append(5)
a[1].remove(1)
a[1] += [6]
print(a)
print(b)

b[2] += (555,)
print(a)
print(b)
