# 用2个栈实现队列
# 栈先进后出 队列先进先出
# 一个栈作为压入栈 压入数据的时候只能从这个栈压入，记为stack_push；另一个作为弹出栈，只从这个栈弹出，记为stack_pop
# 重点：1。stack_push往stack_pop压入数据的时候 必须一次性把stack_push中数据全部压入
# 2。stack_pop如果不为空，stack_push不能向stack_pop中压入数据

class QUEUE(object):
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def add(self, val):
        self.stack_push.append(val)

    # 弹出队首元素
    def poll(self):
        if not self.stack_push and not self.stack_pop:
            print('now is empty stack!')
            return
        elif not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()

    # 查询队首元素
    def peek(self):
        if not self.stack_push and not self.stack_pop:
            print('now is empty stack!')
            return
        elif not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop[-1]


if __name__ == '__main__':
    q = QUEUE()
    for i in range(5):
        q.add(i)
    print(q.poll())
    print(q.peek())
