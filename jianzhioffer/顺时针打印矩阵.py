def shun(alist):
    return alist and [*alist.pop(0)] + shun([*zip(*alist)][::-1])

a= [[1,2,3],[4,5,6],[7,8,9]]
print(shun(a))
