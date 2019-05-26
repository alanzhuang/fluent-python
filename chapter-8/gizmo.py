class Gizmo:
    def __init__(self):
        print('Gizmo id:%d' % id(self))


x = Gizmo()
# 打印Gizmo id:4522902584

y = Gizmo() * 100
# 打印 Gizmo id:4524253648 后再报错
