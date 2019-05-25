a = 3


def test():
    print(a)
    a = 4

def test2():
    global a
    print(a)
    a = 4