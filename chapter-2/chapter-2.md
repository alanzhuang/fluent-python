## 数据结构

### 内置序列类型
容器序列：list,tuple,collections.deque 能够存放不同类型的数据

扁平序列：str,bytes,bytearray,memoryview,array.array 只能容纳一种类型

`容器序列存放的是任意类型的值的引用，扁平序列存放的是值。扁平序列其实是一段连续的内存空间`

可变序列：list,bytearray,array.array,collections.deque,memoryview

不可变序列：tuple,str和bytes

### 列表推导
列表推导不会再有内存泄露问题&nbsp;&nbsp;&nbsp;&nbsp;`listcomps.py`

把列表推导的方括号变成圆括号就是生成器了&nbsp;&nbsp;&nbsp;&nbsp;`clothes.py`

元组拆包：a, b = ('alan', 'zhuang')

a, b = b, a 根本原因是因为2者交换的是`引用的地址`

### 切片
反转字符串 a='look'  a\[::-1\] = 'kool'

### 排序
list.sort就地排序列表 所以返回值为None, sorted会新建一个列表作为返回值


+= *= 对于可变序列会就地修改 对于不可变序列会生成新序列(没有+=)