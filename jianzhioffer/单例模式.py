class Singleton(object):
    def foo(self):
        pass


singleton = Singleton()

# 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
# from a import singleton

# 当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），实例化对象；
# 然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式
import threading
import time

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                # if not hasattr(Singleton, "_instance"):
                Singleton._instance = object.__new__(cls)
        return Singleton._instance


def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
