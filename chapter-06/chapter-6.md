## 设计模式

### 策略对象是很好的享元
享元是可共享的对象，可以同时在多个上下文中使用。

共享是推荐的做法，这样不必在每个新的上下文（shopping.py中的order实例）中使用相同策略时不断新建具体策略对象
