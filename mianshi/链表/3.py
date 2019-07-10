# 约瑟夫问题
def LastRemaining_Solution(n, m):
    if n < 1:
        return -1
    con = list(range(1, n + 1))
    final = -1
    start = 0
    while con:
        k = (start + m - 1) % n
        final = con.pop(k)
        print(final)
        n -= 1
        start = k
    return final


LastRemaining_Solution(5, 3)


# 环形单链表的约瑟夫问题 i节点数，m选择的报到数
# f(n,m) = (f(n-1,m)+m-1)%i+1
def getLive(i, m):
    if i == 1:
        return 1
    else:
        return (getLive(i - 1, m) + m - 1) % i + 1


def LastRemaining_Solution2(head, m: int):
    cur = head.next
    tmp = 1
    while cur != head:
        tmp += 1
        cur = cur.next
    tmp = getLive(tmp, m)
    while tmp > 1:
        head = head.next
        tmp -= 1
    return head
