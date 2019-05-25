r = []


def register(func):
    print('running register(%s)' % (func))
    r.append(func)
    return func


# def register(func):
#     def test():
#         print('running register(%s)' % (func))
#         r.append(func)
#     return test


@register
def func_1():
    print('func___1111')


@register
def func_2():
    print('func___2222')


def func_3():
    print('func___3333')


def main():
    print('start...........')
    print(r)
    func_1()
    func_2()
    func_3()


if __name__ == '__main__':
    main()
