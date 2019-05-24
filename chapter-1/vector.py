class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)


v = Vector()
print(v)

# %r和%s的区别：%r会重现所表达的对象，%s会将所有转成字符串
import datetime

d = datetime.date.today()
print("%s" % d)
print("%r" % d)
