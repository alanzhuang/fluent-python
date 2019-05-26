## python数据模型

### 字符串表现形式（vector.py）

repr能把一个对象用字符串的形式表达出来，这就是"字符串表示形式"。repr就是通过__repr__实现的。

### len为什么不是普通方法

为了让python自带的数据结构可以走后门。
如果是python内置类型 (list,str,bytearray...),__len__返回的其实是PyVarObject的ob_size属性,直接读值速度更快。
