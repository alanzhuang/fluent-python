class A:
    count = 1

    def __init__(self, name):
        self.name = name

    @classmethod
    def add_count(cls):
        cls.count += 1

    @staticmethod
    def test(*args):
        print(args)


A.add_count()
A.add_count()
print(A.count)
A.test()
