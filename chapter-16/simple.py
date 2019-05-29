def simple_coroutine():
    print('start')
    x = yield
    print('get:', x)
s = simple_coroutine()
print('------------')
next(s)
print('------------')
s.send('0000000')
