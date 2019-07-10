# 实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作

# 要求1：pop,push,getMin时间复杂度都是O(1) ------pop,push本来就是O(1)

# 一个栈存放所有元素stack_raw，另一个栈存法每一步的最小值 stack_min
# 新来一个数 如果stack_min为空 那么stack_min也push这个数字
# 如果stack_min不为空 比较stack_min栈顶元素和这个新数 如果这个新数字小于等于栈顶元素 那么stack_min也push这个数

# 额外补充：pyListObject是python提供对列表的抽象
# pyListObject包含了ob_item指针和allocated数值。指针指向了元素列表所在的内存块的首地址,而allocated维护了当前列表可容纳元素总数
# 每一次申请内存时候pyListObject先申请一大块内存，总内存大小记录在allocate，实际使用的内存数量记录在ob_size中
# 根据这种特性 所以只要和列表索引有关的时间复杂度都是O(1) pop,push默认索引都是最后一个 所以时间复杂度都是O(1)


class STACK:
    def __init__(self):
        self.stack_raw = []
        self.stack_min = []

    def pop(self):
        if not self.stack_raw:
            print('now is empty stack!')
        else:
            val = self.stack_raw.pop()
            if val == self.stack_min[-1]:
                self.stack_min.pop()

    def push(self, newNum):
        self.stack_raw.append(newNum)
        if not self.stack_min:
            self.stack_min.append(newNum)
        elif self.stack_min[-1] >= newNum:
            self.stack_min.append(newNum)

    def getMin(self):
        if self.stack_min:
            return self.stack_min[-1]
        else:
            print('now is empty stack!')

if __name__ == '__main__':
    q = STACK()
    q.push(3)
    print(q.getMin())