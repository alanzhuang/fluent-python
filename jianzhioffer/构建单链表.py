# 单链表实现


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLink(object):
    def __init__(self):
        # 头节点
        self.__head = None

    def __len__(self):
        if self.is_empty():
            return 0
        else:
            count = 1
            cur = self.__head
            while cur.next is not None:
                count += 1
                cur = cur.next
            return count

    def is_empty(self):
        return self.__head is None

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next

    def add(self, val):
        node = Node(val)
        node.next = self.__head
        self.__head = node

    def append(self, val):
        node = Node(val)
        if self.is_empty():
            self.__head = node
        else:
            # cur就是游标
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    # 单链反转 画单链图有助于理解
    def reverse(self):
        L, M = None, self.__head
        while M is not None:
            R = M.next
            M.next = L
            L = M
            M = R
        # R.next = M
        self.__head = L


if __name__ == '__main__':
    a = SingleLink()
    a.append(2)
    a.append(3)
    a.append(4)
    a.add(333)
    print(len(a))
    print(a.travel())
    a.reverse()
    print(a.travel())
