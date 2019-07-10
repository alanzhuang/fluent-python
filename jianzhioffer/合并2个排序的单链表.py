# class Node(object):
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#


def merge(p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    p = None
    if p1.val > p2.val:
        p = p2
        p.next = merge(p1, p2.next)
    else:
        p = p1
        p.next = merge(p2, p1.next)

    return p
